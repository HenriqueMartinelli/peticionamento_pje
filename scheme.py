# Dictionary with the description of the site screens,
# each screen has an indication of screen, available actions and elements for interaction

def SCHEME(num_termo=None, qtdDoc=None, arquivo=None, files=None, ViewState=None, 
            peticionarUrl=None, inputs=dict(), numero_processo='00000000000000000',
            idProcesso=None, idPeticionar=None, hash_=None, username=None, password=None, captcha=None):
    return {
        "Login": {
                "requests": [{
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/logar.seam",
                            "decode": False,
                            "update_form": True,
                            "files": {},
                            "payload":{
                                        'username': username,
                                        'password': password,
                                        'newPassword1': '',
                                        'newPassword2': '',
                                        'g-recaptcha-response': captcha, 
                                        'h-captcha-response': captcha,
                                    },
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                                        'Origin': 'https://pje.tjba.jus.br',
                                        'Referer': 'https://pje.tjba.jus.br/pje/login.seam?loginComCertificado=false',
                                        },
                            "params": {}
                            }],
                "expected_message": {
                                "tag": "span", "type": "class", "value": "rich-messages-label",
                                "expected_text": None,
                                "expected_url": "QuadroAviso/listViewQuadroAvisoMensagem.seam",
                                "not_expected": ["A verificação de captcha"]},
        "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': 'https://pje.tjba.jus.br',
                            'Host': 'pje.tjba.jus.br',
                            'Referer': peticionarUrl,
                            },
                "payload": {
                            'AJAXREQUEST': inputs.get('AjaxRequest'),
                            'formularioUpload': 'formularioUpload',
                            'cbTDDecoration:cbTD': num_termo,
                            'ipDescDecoration:ipDesc': 'ALEGAÇÕES FINAIS',
                            'raTipoDocPrincipal': 'HTML',
                            'docPrincipalEditorTextArea': '<p>em ANEXOOOOO</p>',
                            'context': '/pje',
                            'cid': inputs.get('cid'),
                            'mimes': inputs.get('mimes'),
                            'quantidadeProcessoDocumento': inputs.get('qtdDoc'),
                            'j_id223:0:ordem': '1',
                            'j_id223:0:numeroDoc': '',
                            'mimesEhSizes': inputs.get('mimesEhSizes'),
                            'tipoDocLoteSuperior': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                            'javax.faces.ViewState': inputs.get('ViewState')
                             } 
        },
        "ScheduleRequestForm": {
                "requests": [{
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
                                        f"j_id223:{inputs.get('qtdDoc')}:tipoDoc": num_termo,
                                        f"j_id223:{inputs.get('qtdDoc')}:j_id254": f"j_id223:{inputs.get('qtdDoc')}:j_id254",
                                        "ajaxSingle": f"j_id223:{inputs.get('qtdDoc')}:tipoDoc"
                                        },
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/seam/resource/upload",
                            "decode": False,
                            "update_form": True,
                            "files": files,
                            "payload":{
                                        "j_id202": "Salvar",
                                        "j_id223:0:descDoc": arquivo,
                                        "j_id223:0:numeroDoc": ""},
                            "headers":{
                                        'X-Requested-With': 'XMLHttpRequest',
                                        'Accept': 'application/json'},
                            "params": {
                                        'cid': inputs.get('cid'),
                                        'isLibreOffice': 'undefined' }
                            },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
                                        "j_id223:0:numeroDoc": "",
                                        f"j_id223:{inputs.get('qtdDoc')}:commandLinkAtualizarComboTipoDocumento": f"j_id223:{inputs.get('qtdDoc')}:commandLinkAtualizarComboTipoDocumento",
                                        "ajaxSingle": f"j_id223:{inputs.get('qtdDoc')}:commandLinkAtualizarComboTipoDocumento"
                                        },
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
                                        "j_id223:0:numeroDoc": "",
                                        f"j_id223:{inputs.get('qtdDoc')}:commandLinkGravar": f"j_id223:{inputs.get('qtdDoc')}:commandLinkGravar",
                                        "ajaxSingle": f"j_id223:{inputs.get('qtdDoc')}:commandLinkGravar"
                                        },
                            "headers": {},
                            "params": {}
                                }
                            ],
                "expected_message": {
                                "tag": "span", "type": "class", "value": "rich-messages-label",
                                "expected_text": 'finalizado o upload do arquivo'},
        },
        "PrepareUpload": {
                "requests": [{
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'formularioUpload': 'formularioUpload',
                                        'cbTDDecoration:cbTD': num_termo,
                                        'ipDescDecoration:ipDesc': 'Conclusão',
                                        'ipNroDecoration:ipNro': '',
                                        'raTipoDocPrincipal': 'HTML',
                                        'docPrincipalEditorTextArea': '<p>em anexo</p>',
                                        'javax.faces.ViewState':ViewState,
                                        'j_id202': 'j_id202',
                                        'AJAX:EVENTS_COUNT': '1'
                                    },
                            "headers": {},
                            "params": {}
                                }],
            },
        "SearchLinks": {
                "requests": [{
                            "method": "GET", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                            "decode": False,
                            "files": {},
                            "payload":{},
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Host': 'pje.tjba.jus.br',
                                        'Origin': 'https://pje.tjba.jus.br',
                                    },
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                            "decode": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'fPP:numeroProcesso:numeroSequencial': numero_processo[:-13],
                                        'fPP:numeroProcesso:numeroDigitoVerificador': numero_processo[-13:-11],
                                        'fPP:numeroProcesso:Ano': numero_processo[-11:-7],
                                        'fPP:numeroProcesso:ramoJustica': numero_processo[-7:-6],
                                        'fPP:numeroProcesso:respectivoTribunal': numero_processo[-6:-4],
                                        'fPP:numeroProcesso:NumeroOrgaoJustica': numero_processo[-4:],
                                        'fPP': 'fPP',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': ViewState,
                                        'conversationPropagation': 'join',
                                        'fPP:searchProcessosPeticao': 'fPP:searchProcessosPeticao',
                                        'AJAX:EVENTS_COUNT': '1'
                                    },
                            "headers": {
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Host': 'pje.tjba.jus.br',
                                        'Origin': 'https://pje.tjba.jus.br',
                                        'Referer': 'https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam',
                                    },
                            "params": {}
                            },
                                                        {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                            "decode": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'fPP:numeroProcesso:numeroSequencial': numero_processo[:-13],
                                        'fPP:numeroProcesso:numeroDigitoVerificador': numero_processo[-13:-11],
                                        'fPP:numeroProcesso:Ano': numero_processo[-11:-7],
                                        'fPP:numeroProcesso:ramoJustica': numero_processo[-7:-6],
                                        'fPP:numeroProcesso:respectivoTribunal': numero_processo[-6:-4],
                                        'fPP:numeroProcesso:NumeroOrgaoJustica': numero_processo[-4:],
                                        'fPP': 'fPP',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': ViewState,
                                        'conversationPropagation': 'join',
                                        'fPP:searchProcessosPeticao': 'fPP:searchProcessosPeticao',
                                        'AJAX:EVENTS_COUNT': '1',
                                        'javax.faces.ViewState':ViewState,
                                        'idProcesso': idProcesso,
                                        idPeticionar: idPeticionar,
                                        'ajaxSingle': idPeticionar
                                    },
                            "headers": {
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Host': 'pje.tjba.jus.br',
                                        'Origin': 'https://pje.tjba.jus.br',
                                        'Referer': 'https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam',
                                    },
                            "params": {}
                            },
                            {
                            "method": "GET", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": False,
                            "files": {},
                            "payload":{},
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Host': 'pje.tjba.jus.br',
                                        'Origin': 'https://pje.tjba.jus.br',
                                    },
                            "params": {
                                        'idProcesso': idProcesso,
                                        'ca': hash_}
                                },
                    
                                
                                ],
        }
    }}
