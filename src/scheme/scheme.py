# Dictionary with the description of the site screens,
# each screen has an indication of screen, available actions and elements for interaction

def SCHEME(inputs=dict(), arquivo=None, files=None, 
            peticionarUrl=None, username=None, password=None, captcha=None):
    idProcesso = inputs.get('idProcesso')
    return {
        "Login": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/logar.seam",
                            "decode": False,
                            "update_form": False,
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
                                        'Origin': inputs.get('domain'),
                                        'Referer': f"{inputs.get('URL_BASE')}/login.seam?loginComCertificado=false",
                                        },
                            "params": {}
                            }],
                "expected_message": {
                                "tag": "",
                                "expected_text": '',
                                "not_expected_url": "",
                                "expected_url": "QuadroAviso/listViewQuadroAvisoMensagem.seam",
                                "not_expected": ["A verificação de captcha"]},
                    },
        "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Host': inputs.get('domain').split('//')[1],
                            'Referer': peticionarUrl,
                            },
                "payload": {
                            'AJAXREQUEST': inputs.get('AjaxRequest'),
                            'formularioUpload': 'formularioUpload',
                            'cbTDDecoration:cbTD': inputs.get('num_termo'),
                            'ipDescDecoration:ipDesc': inputs.get('ipDesc'),
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
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
                                        f"j_id223:{inputs.get('qtdDoc')}:tipoDoc": inputs.get('num_anexo'),
                                        f"j_id223:{inputs.get('qtdDoc')}:j_id254": f"j_id223:{inputs.get('qtdDoc')}:j_id254",
                                        "ajaxSingle": f"j_id223:{inputs.get('qtdDoc')}:tipoDoc"
                                        },
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/seam/resource/upload",
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
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
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
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
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
                                "expected_text": 'finalizado o upload do arquivo',
                                "expected_url": "",
                                "not_expected_url": "/pje/errorUnexpected.seam?",
                                "not_expected": ["Failed to process the request", "Erro ao tentar gravar o arquivo"]},
                        },
        "PrepareUpload": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'formularioUpload': 'formularioUpload',
                                        'cbTDDecoration:cbTD': inputs.get('num_termo'),
                                        'ipDescDecoration:ipDesc': inputs.get('ipDesc'),
                                        'ipNroDecoration:ipNro': '',
                                        'raTipoDocPrincipal': 'HTML',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        "cbTDDecoration:cbTD": inputs.get('num_termo'),
                                        "cbTDDecoration:j_id81": "cbTDDecoration:j_id81",
                                        "ajaxSingle": "cbTDDecoration:cbTD",
                                        "AJAX:EVENTS_COUNT": "1"
                                    },
                            "headers": {
                                        'Accept': '*/*',
                                        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Origin': inputs.get('domain'),
                                        'Host': inputs.get('domain').split('//')[1],
                                        'Referer': peticionarUrl,
                                        },
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "update_form": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'formularioUpload': 'formularioUpload',
                                        'cbTDDecoration:cbTD': inputs.get('num_termo'),
                                        'ipDescDecoration:ipDesc': inputs.get('ipDesc'),
                                        'ipNroDecoration:ipNro': '',
                                        'raTipoDocPrincipal': 'HTML',
                                        'docPrincipalEditorTextArea': '<p>em anexo</p>',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'j_id202': 'j_id202',
                                        'AJAX:EVENTS_COUNT': '1'
                                    },
                            "headers": {
                                        'Accept': '*/*',
                                        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Origin': inputs.get('domain'),
                                        'Host': inputs.get('domain').split('//')[1],
                                        'Referer': peticionarUrl,
                                        },
                            "params": {}
                                }],
                        },
        "SearchLinks": {
                "requests": [{
                            "method": "GET", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                            "decode": False,
                            "files": {},
                            "payload":{},
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Host': inputs.get('domain').split('//')[1],
                                        'Origin': inputs.get('domain'),
                                    },
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                            "decode": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'fPP:numeroProcesso:numeroSequencial': inputs['processo'][:-13],
                                        'fPP:numeroProcesso:numeroDigitoVerificador': inputs['processo'][-13:-11],
                                        'fPP:numeroProcesso:Ano': inputs['processo'][-11:-7],
                                        'fPP:numeroProcesso:ramoJustica': inputs['processo'][-7:-6],
                                        'fPP:numeroProcesso:respectivoTribunal': inputs['processo'][-6:-4],
                                        'fPP:numeroProcesso:NumeroOrgaoJustica': inputs['processo'][-4:],
                                        'fPP': 'fPP',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'conversationPropagation': 'join',
                                        'fPP:searchProcessosPeticao': 'fPP:searchProcessosPeticao',
                                        'AJAX:EVENTS_COUNT': '1'
                                    },
                            "headers": {
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Host': inputs.get('domain').split('//')[1],
                                        'Origin': inputs.get('domain'),
                                        'Referer': f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                                    },
                            "params": {}
                            },
                                                        {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                            "decode": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'fPP:numeroProcesso:numeroSequencial': inputs['processo'][:-13],
                                        'fPP:numeroProcesso:numeroDigitoVerificador': inputs['processo'][-13:-11],
                                        'fPP:numeroProcesso:Ano': inputs['processo'][-11:-7],
                                        'fPP:numeroProcesso:ramoJustica': inputs['processo'][-7:-6],
                                        'fPP:numeroProcesso:respectivoTribunal': inputs['processo'][-6:-4],
                                        'fPP:numeroProcesso:NumeroOrgaoJustica': inputs['processo'][-4:],
                                        'fPP': 'fPP',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'conversationPropagation': 'join',
                                        'fPP:searchProcessosPeticao': 'fPP:searchProcessosPeticao',
                                        'AJAX:EVENTS_COUNT': '1',
                                        'javax.faces.ViewState':inputs.get('ViewState'),
                                        'idProcesso': inputs.get('idProcesso'),
                                        f'fPP:processosTable:{idProcesso}:idPet': f'fPP:processosTable:{idProcesso}:idPet',
                                        'ajaxSingle': f'fPP:processosTable:{idProcesso}:idPet'
                                    },
                            "headers": {
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Host': inputs.get('domain').split('//')[1],
                                        'Origin': inputs.get('domain'),
                                        'Referer': f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoavulsa.seam",
                                    },
                            "params": {}
                            },
                            {
                            "method": "GET", 
                            "url":f"{inputs.get('URL_BASE')}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": False,
                            "files": {},
                            "payload":{},
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Host': inputs.get('domain').split('//')[1],
                                        'Origin': inputs.get('domain'),
                                    },
                            "params": {
                                        'idProcesso': inputs.get('idProcesso'),
                                        'ca': inputs.get('hash_')}
                                },
                    
                                
                                ],
        }
    }
