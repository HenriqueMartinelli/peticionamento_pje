# Dictionary with the description of the site screens,
# each screen has an indication of screen iframe, available actions and elements for interaction

def SCHEME(num_termo=None, qtdDoc=None, arquivo=None, cid=None, files=None,
           ViewState=None, peticionarUrl=None, inputs=None):
    return {
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
                            'AJAXREQUEST': inputs['AjaxRequest'],
                            'formularioUpload': 'formularioUpload',
                            'cbTDDecoration:cbTD': num_termo,
                            'ipDescDecoration:ipDesc': 'ALEGAÇÕES FINAIS',
                            'raTipoDocPrincipal': 'HTML',
                            'docPrincipalEditorTextArea': '<p>em ANEXOOOOO</p>',
                            'context': '/pje',
                            'cid': inputs['cid'],
                            'mimes': inputs['mimes'],
                            'quantidadeProcessoDocumento': inputs['qtdDoc'],
                            'j_id223:0:ordem': '1',
                            'j_id223:0:numeroDoc': '',
                            'mimesEhSizes': inputs['mimesEhSizes'],
                            'tipoDocLoteSuperior': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                            'javax.faces.ViewState': inputs['ViewState']
                             } 
        },
        "ScheduleRequestForm": {
                "requests": [{
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "files": {},
                            "payload":{
                                        f"j_id223:{inputs['qtdDoc']}:tipoDoc": num_termo,
                                        f"j_id223:{inputs['qtdDoc']}:j_id254": f"j_id223:{inputs['qtdDoc']}:j_id254",
                                        "ajaxSingle": f"j_id223:{inputs['qtdDoc']}:tipoDoc"
                                        },
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/seam/resource/upload",
                            "decode": False,
                            "files": files,
                            "payload":{
                                        "j_id202": "Salvar",
                                        "j_id223:0:tipoDoc": num_termo,
                                        "j_id223:0:descDoc": arquivo,
                                        "j_id223:0:numeroDoc": ""},
                            "headers":{
                                        'X-Requested-With': 'XMLHttpRequest',
                                        'Accept': 'application/json'},
                            "params": {
                                        'cid': inputs['cid'],
                                        'isLibreOffice': 'undefined' }
                            },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "files": {},
                            "payload":{
                                        "j_id223:0:numeroDoc": "",
                                        # 'quantidadeProcessoDocumento': qtdDoc,
                                        f"j_id223:{inputs['qtdDoc']}:commandLinkAtualizarComboTipoDocumento": f"j_id223:{qtdDoc}:commandLinkAtualizarComboTipoDocumento",
                                        "ajaxSingle": f"j_id223:{inputs['qtdDoc']}:commandLinkAtualizarComboTipoDocumento"
                                        },
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
                            "files": {},
                            "payload":{
                                        "j_id223:0:numeroDoc": "",
                                        f"j_id223:{inputs['qtdDoc']}:commandLinkGravar": f"j_id223:{inputs['qtdDoc']}:commandLinkGravar",
                                        "ajaxSingle": f"j_id223:{inputs['qtdDoc']}:commandLinkGravar"},
                            "headers": {},
                            "params": {}
                                }
                            ]
        },
        "PrepareUpload": {
                "requests": [{
                            "method": "POST", 
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": True,
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
                            "url": "https://pje.tjba.jus.br/pje/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
                            "decode": False,
                            "files": {},
                            "payload":{},
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Host': 'pje.tjba.jus.br',
                                        'Origin': 'https://pje.tjba.jus.br',
                                    },
                            "params": {}
                                }],
        }
    }
