
import requests
import base64
import magic
import io
import mimetypes

from typing import Union, List
from fastapi import FastAPI, Request
from src.pje_pet import Pje_pet, MainClientException

client = Pje_pet()
app = FastAPI()
session = requests.session()


@app.post("/upload")
async def upload(request: Request):
    try:
        form = await request.json()
        content = get_content(content=form, required_fields=["tipo", "files", "processo", "idProcesso",
                                                             "username", "password", "idTarefa", "instancia"])
        
        client.set_global_variable(len(content['files']), content['idTarefa'], content['processo'], content['instancia'])
        client.login(username=content['username'], password=content['password'], session=session)

        for num, file in enumerate(content['files']):
            mime, mimetype, file_size = get_extension(file['b64Content'])
            decode_file = base64.b64decode(file['b64Content'])
            client.start(content=content, mimetype=mimetype, file=decode_file, mime=mime,
                         file_size=file_size, cont=num+1, file_options=file)
            
        return {"sucesso" : True}
    
    except MainClientException as e:
        client.returnMsg(msg=F"Fatal Error: {e}", error= True, forced=True)
        return error(e.args[0])
    except Exception as e:
        client.returnMsg(msg=F"Fatal Error: {e}", error= True, forced=True)
        return error(msg=e.args[0]) 


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