import json
import urllib
from bs4 import BeautifulSoup
from scheme import SCHEME
from datetime import datetime


class BaseRequest:
    def __init__(self,
                 base_url: str = "http://refor.detran.rj.gov.br/"):
        
        self.URL_BASE = 'http://refor.detran.rj.gov.br/'



    def search_inputs(self, content):
        soup = BeautifulSoup(content, "html.parser")
        return {
            "cid" :soup.find('input', {'name': 'cid'})['value'],
            "mimes" : soup.find('input', {'name': 'mimes'})['value'],
            "mimesEhSizes" : soup.find('input', {'name': 'mimesEhSizes'})['value'],
            "AjaxRequest" : soup.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':'")[1].split("',")[0],
            "qtdDoc" : soup.find('input', {'id': 'quantidadeProcessoDocumento'})['value'],
            "ViewState": soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        }


    def switch_to_screen(self, screen: str):
            self.current_screen = screen

    def event_expected(self, screen, response):
        msg = str()
        data = SCHEME()[screen]['expected_message']
        soup = BeautifulSoup(response.content, "html.parser")
        if data.get('tag'):
            text_result = soup.find(data['tag'], {data['type']: data['value']}).text.strip().lower()
            if data['expected_text'] in text_result:
                self.returnMsg(msg, error=False, response=response)
            elif data['not_expected'] in text_result:
                self.returnMsg(msg, error=True, response=response)
            elif data['expected_url'] in response.url:
                self.returnMsg(msg, error=False, response=response)

         

    def returnMsg(self, msg, error, response):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        event = {
                "event":{  
                "screen":self.current_screen,
                "created_at":dt_string,
                "data":{
                        "msg": msg,
                        "error": error,
                        "status_code": response.status_code
                }}}
        return event
                

    @staticmethod
    def screen_decorator(screen: str):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if self.current_screen != screen:
                    raise Exception(f"Need to be on {screen} screen: {self.current_screen}")
                return func(self, *args, **kwargs)

            return wrapper

        return decorator


    def find_text(self, text=str):
        with open('itens.json') as f:
            js = json.load(f)
        return js[text]
    

    def add_schedule(self, qtddoc, descDoc, tipoDoc):
        return [
            (f'j_id223:{qtddoc}:ordem', '2'),
            (f'j_id223:{qtddoc}:descDoc', descDoc),
            (f'j_id223:{qtddoc}:numeroDoc', ''),
            (f'j_id223:{qtddoc}:tipoDoc', tipoDoc) 
            ]
        
    def request(self, method, url, decode:bool, headers=None, payload=None, params=None, files=None):
            if decode:
                payload = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
            if files != {}: 
                del headers['Content-Type']
            return self.session.request(method, url=url, params=params,
                                  headers=headers, data=payload, files=files
                                )
    
    def update_form(self, tipoDoc, payload, headers, qtdDoc=0, descDoc=None, ):
            scheme = SCHEME(inputs=self.inputs, num_termo=tipoDoc, peticionarUrl=self.peticionarHTML.url)
            payloadUpdate = scheme['GlobalForm']['payload']
            headersUpdate = scheme['GlobalForm']['headers']
            payloadUpdate.update(payload), headersUpdate.update(headers)
            if int(qtdDoc) > 0:
                payload = [(key, payload[key]) for key in payload]
                payload = payload + self.add_schedule(descDoc=descDoc, tipoDoc=tipoDoc, qtddoc=qtdDoc)
            return payloadUpdate, headersUpdate
    

    def find_locator(self, element:str, arquivo=None, num_termos=None,  files=None, inputs=None,
                     username=None, password=None, captcha=None):
        screen = self.current_screen
        datas = SCHEME(num_termo=num_termos, inputs=inputs, arquivo=arquivo, 
                       files=files, username=username, password=password, captcha=captcha)[screen][element]
        for data in datas:
            if datas['update_form']:
                payload, headers = self.update_form(qtdDoc=inputs['qtdDoc'], descDoc=arquivo, 
                                                    tipoDoc=num_termos, payload=data['payload'], headers=data['headers'])
            
            response = self.request(method=data['method'], 
                         url=data['url'], payload=payload, 
                         headers=headers, params=data['params'],
                         decode=data['decode'], files=data['files'])
            
            if 'finalizado' in response.text.lower():
                print('ENVIADO')
        return response
    