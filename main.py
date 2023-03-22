
import requests
import base64
import base64
import magic
import io
import mimetypes

from typing import Union, List
from fastapi import FastAPI, Request
from crawler import crawler, MainClientException

client = crawler()
app = FastAPI()
session = requests.session()

### ARRUMAR OS PONTOS DO PROCESSO
@app.post("/upload")
async def upload(request: Request):
    try:
        form = await request.json()
        content = get_content(content=form, required_fields=["tipo", "files", "processo", "username", "password"])
        client.login(username=content['username'], password=content['password'], session=session)

        for num, file in enumerate(content['files']):
            mime, mimetype, file_size = get_extension(file)
            decode_file = base64.b64decode(file)
            parametro = client.find_text(content['tipo'])

            client.search_links(numero_processo=content['processo'].strip(), session=session)
            client.prepare_upload(num_termo=parametro)
            client.schedule_request(filename=f"anexo{num}{mimetype}", file=decode_file, 
                                    num_termo=parametro, mime=mime, file_size=file_size, mimetype=mimetype)
        
        return {"message": f"Successfully uploaded files"}
    except MainClientException as e:
        return error(e.args[0])
    except:
        return error() 


#   Utils
###################################################################
def get_extension(str_base64):
    bytesData = io.BytesIO()
    bytesData.write(base64.b64decode(str_base64))
    bytesData.seek(0)
    mime = magic.from_buffer(bytesData.read(), mime=True)
    mimetype = mimetypes.guess_extension(mime)
    file_size = (len(str_base64) * 6 - str_base64.count('=') * 8) / 8
    return mime, mimetype, file_size

def get_content(content, required_fields):
    validate_content(content, required_fields)
    return content

def validate_content(content, required_fields):
    for field in required_fields:
        if field not in content:
            raise MainClientException("Requisição inválida.")

def error(msg="Erro desconhecido ao processar requisição."):
    return {
        "sucesso" : False,
        "msg": msg
    }
            

def invalid_request():
    return error(msg="Requisição inválida.")

def ok():
    return {
        "sucesso" : True
    }