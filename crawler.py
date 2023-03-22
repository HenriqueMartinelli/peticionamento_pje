import requests 
import json
import os
from twocaptcha import TwoCaptcha
from bs4 import BeautifulSoup
from anticaptchaofficial.hcaptchaproxyless import *
from base import BaseRequest
from scheme import SCHEME
from datetime import datetime

class MainClientException(Exception):
    pass

class crawler(BaseRequest):
    def antiCaptcha(self):
        solver = hCaptchaProxyless()
        solver.set_verbose(1)
        solver.set_key("fa901ee28ac52b82d466a87985a19092")
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
                                        password=password, captcha=captcha)
            print(self.event_expected("Login", response_login))

        self.switch_to_screen("SearchLinks")
        return response_login


    @BaseRequest.screen_decorator("SearchLinks")
    def search_links(self, numero_processo:str, session):
        self.session = session

        data = SCHEME()[self.current_screen]["requests"][0]
        get_ViewState = self.request(method=data['method'], 
                         url=data['url'], payload=data['payload'], 
                         headers=data['headers'], params=data['params'],
                         decode=data['decode'], files=data['files'])

        soup = BeautifulSoup(get_ViewState.content, 'html.parser')
        ViewState = soup.find(
            'input', {'id': 'javax.faces.ViewState'})['value']

        data = SCHEME(ViewState=ViewState, numero_processo=numero_processo)[self.current_screen]["requests"][1]
        responseSearch = self.request(method=data['method'], 
                                    url=data['url'], payload=data['payload'], 
                                    headers=data['headers'], params=data['params'],
                                    decode=data['decode'], files=data['files'])
        soup = BeautifulSoup(responseSearch.content, 'html.parser')
        idPeticionar = soup.find('a', {'title': 'Peticionar'})['id']
        idProcesso = idPeticionar.split(':')[-2]



        data = SCHEME(ViewState=ViewState, idProcesso=idProcesso, idPeticionar=idPeticionar)[self.current_screen]["requests"][2]
        response_hash = self.request(method=data['method'], 
                                    url=data['url'], payload=data['payload'], 
                                    headers=data['headers'], params=data['params'],
                                    decode=data['decode'], files=data['files'])
        

        hash_ = response_hash.text.split('&')[1].split('"')[0].split('=')[-1]

        data = SCHEME(ViewState=ViewState, idProcesso=idProcesso, hash_=hash_)[self.current_screen]["requests"][3]
        self.peticionarHTML = self.request(method=data['method'], 
                                            url=data['url'], payload=data['payload'], 
                                            headers=data['headers'], params=data['params'],
                                            decode=data['decode'], files=data['files'])
        self.switch_to_screen("PrepareUpload")
        return self.peticionarHTML
    

    @BaseRequest.screen_decorator("ScheduleRequestForm")
    def schedule_request(self, filename, file, num_termo:str, mimetype:str, mime:str, file_size):
        payload = {
                    'quantidadeProcessoDocumento': self.inputs['qtdDoc'],
                    'jsonProcessoDocumento': {"array":json.dumps([{'nome': filename, 'tamanho': int(str(file_size).split('.')[0]), 'mime': '.pdf'}])},
                    'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
                    'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
                    'AJAX:EVENTS_COUNT': '1'}

        payload, headers = self.update_form(tipoDoc=num_termo, payload=payload, headers={})
        self.request(method='POST', 
                    url='https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam',
                    payload=payload,  headers=headers, 
                    params={}, decode=True, files={})

        files = {filename: file}
        response = self.find_locator('requests', num_termos=num_termo, arquivo=filename, files=files, inputs=self.inputs)
        return response

    @BaseRequest.screen_decorator("PrepareUpload")
    def prepare_upload(self, num_termo):
        if not 'commandLinkAdicionar' in self.peticionarHTML.text:
                self.find_locator('requests', inputs=self.inputs, num_termos=num_termo)
        self.inputs = self.search_inputs(self.peticionarHTML.content)
        self.switch_to_screen("ScheduleRequestForm")
