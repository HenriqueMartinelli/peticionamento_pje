import requests 
import json
from bs4 import BeautifulSoup
from anticaptchaofficial.hcaptchaproxyless import *
from src.init import BaseRequest
from src.scheme.scheme import SCHEME
from datetime import datetime

class MainClientException(Exception):
    pass

class Pje_pet(BaseRequest):
    def antiCaptcha(self):
        solver = hCaptchaProxyless()
        solver.set_verbose(1)
        solver.set_key("YOUR-TOKEN")
        solver.set_website_url("https://pje.tjba.jus.br/")
        solver.set_website_key('4098ab2e-d12a-40a8-b836-46df3b32df3f')
        result = solver.solve_and_return_solution()
        return result


    def login(self, username, password, session) -> str:
        self.switch_to_screen("Login")
        for i in range(3):
            self.session = session
            captcha = self.antiCaptcha()
            response_login = self.find_locator('requests', username=username, 
                                        password=password, captcha=captcha, inputs=self.inputs)
            login = self.event_expected("Login", response_login)
            if not login:
                break
        if login:
            raise ValueError('Error in login requests')
        
        return self.switch_to_screen("SearchLinks")



    @BaseRequest.screen_decorator("SearchLinks")
    def search_links(self, idProcesso):
        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][0]
        get_ViewState = self.request(method=data['method'], 
                         url=data['url'], payload=data['payload'], 
                         headers=data['headers'], params=data['params'],
                         decode=data['decode'], files=data['files'])

        soup = BeautifulSoup(get_ViewState.content, 'html.parser')
        self.inputs['ViewState'] = soup.find(
            'input', {'id': 'javax.faces.ViewState'})['value']
        
        data = SCHEME(inputs=self.inputs)["SearchLinks"]["requests"][1]
        responseSearch = self.request(method=data['method'], 
                                    url=data['url'], payload=data['payload'], 
                                    headers=data['headers'], params=data['params'],
                                    decode=data['decode'], files=data['files'])
        
        self.inputs['idProcesso'] = self.find_idProcesso(idProcesso=idProcesso, response=responseSearch)
        data = SCHEME(inputs=self.inputs)["SearchLinks"]["requests"][2]
        response_hash = self.request(method=data['method'], 
                                    url=data['url'], payload=data['payload'], 
                                    headers=data['headers'], params=data['params'],
                                    decode=data['decode'], files=data['files'])
        

        self.inputs['hash_'] = response_hash.text.split('&')[1].split('"')[0].split('=')[-1]
        data = SCHEME(inputs=self.inputs)["SearchLinks"]["requests"][3]
        self.peticionarHTML = self.request(method=data['method'], 
                                            url=data['url'], payload=data['payload'], 
                                            headers=data['headers'], params=data['params'],
                                            decode=data['decode'], files=data['files'])
        self.switch_to_screen("PrepareUpload")
        return self.peticionarHTML
    

    @BaseRequest.screen_decorator("ScheduleRequestForm")
    def schedule_request(self, filename, file, mime:str, file_size,):
        payload = {
                    'quantidadeProcessoDocumento': self.inputs['qtdDoc'],
                    'jsonProcessoDocumento': {"array":json.dumps([{'nome': filename, 'tamanho': int(str(file_size).split('.')[0]), 'mime': mime}])},
                    'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
                    'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
                    'AJAX:EVENTS_COUNT': '1'}

        payload, headers = self.update_form(payload=payload, headers={})
        self.request(method='POST', 
                    url=f"{self.inputs['URL_BASE']}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                    payload=payload,  headers=headers, 
                    params={}, decode=True, files={})

        files = {filename: file}
        return self.find_locator('requests', arquivo=filename, files=files, inputs=self.inputs)


    @BaseRequest.screen_decorator("PrepareUpload")
    def prepare_upload(self):
        self.send_editor_text_area()
        self.inputs.update(self.search_inputs(self.peticionarHTML.content))
        self.switch_to_screen("ScheduleRequestForm")


    def send_editor_text_area(self):
        soup = BeautifulSoup(self.peticionarHTML.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        self.find_locator('requests', inputs=self.inputs)
        data = SCHEME(inputs=self.inputs)["SearchLinks"]["requests"][3]
        self.peticionarHTML = self.request(method=data['method'], 
                                            url=data['url'], payload=data['payload'], 
                                            headers=data['headers'], params=data['params'],
                                            decode=data['decode'], files=data['files'])


    def start(self, content, mimetype, file, mime, file_size, cont, file_options):
        self.cont = cont
        self.inputs.update(file_options)
        self.find_text(num_termo=content['tipo'], num_anexo=file_options['tipo_anexo'])
        self.switch_to_screen("SearchLinks")
        self.search_links(content['idProcesso'].strip())
        self.prepare_upload()
        response = self.schedule_request(filename=f"{file_options['filename']}{mimetype}", file=file, 
                                         mime=mime, file_size=file_size)
        self.event_expected("ScheduleRequestForm", response)

  

