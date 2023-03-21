import json
import urllib
from bs4 import BeautifulSoup
from scheme import SCHEME


class BaseRequest:
    def __init__(self,
                 base_url: str = "http://refor.detran.rj.gov.br/"):
        
        self.URL_BASE = 'http://refor.detran.rj.gov.br/'



    def search_inputs(content):
        soup = BeautifulSoup(content, "html.parser")
        return {
            "cid" :soup.find('input', {'name': 'cid'})['value'],
            "mimes" : soup.find('input', {'name': 'mimes'})['value'],
            "mimesEhSizes" : soup.find('input', {'name': 'mimesEhSizes'})['value'],
            "ViewState" : soup.find('input', {'name': 'javax.faces.ViewState'})['value'],
            "AjaxRequest" : soup.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':'")[1].split("',")[0],
            "qtdDoc" : soup.find('input', {'id': 'quantidadeProcessoDocumento'})['value'],
            "ViewState": soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        }


    def switch_to_screen(self, screen: str):
        if screen in SCHEME():
            self.current_screen = screen
        else:
            raise Exception(f"Screen {screen} not found")


    @staticmethod
    def returnMsg(self, infos, msg):
        finally_msg = f"User: {infos.get('usuario')}, Caer:{infos.get('caer')}, Renach: {infos.get('protocolo')}, Return {msg}"
        infos.update({'log': finally_msg})
                

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
    

    def send_request(self, session, headers, payload):
        payload_decode = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        response = session.post(
            url='https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam',
            headers=headers,
            data=payload_decode,
        )


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
    def update_form(self, qtdDoc, descDoc, tipoDoc, payload, headers):
            scheme = SCHEME(inputs=self.inputs, num_termo=tipoDoc, peticionarUrl=self.peticionarHTML)
            payloadUpdate = scheme['GlobalForm']['headers']
            headersUpdate = scheme['GlobalForm']['payload']
            payloadUpdate.update(payload), headersUpdate.update(headers)
            if int(qtdDoc) > 0:
                payload = [(key, payload[key]) for key in payload]
                payload = payload + self.add_schedule(descDoc=descDoc, tipoDoc=tipoDoc, qtddoc=qtdDoc)
            return payloadUpdate, headersUpdate
    

    def find_locator(self, element:str, inputs:dict(), arquivo=None, num_termos=None,  files=None):
        screen = self.current_screen
        datas = SCHEME(num_termo=num_termos, inputs=inputs, arquivo=arquivo, files=files)[screen][element]

        lista = list()
        for data in datas:
            payload, headers = self.update_form(qtdDoc=inputs['qtdDoc'], descDoc=arquivo, 
                                                tipoDoc=num_termos, payload=data['payload'], headers=data['headers'])
            
            r = self.request(method=data['method'], 
                         url=data['url'], payload=payload, 
                         headers=headers, params=data['params'],
                         decode=data['decode'], files=data['files'])
            
            lista.append(r.text)
            if 'finalizado' in r.text.lower():
                print('ENVIADO')
        return lista