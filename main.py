
import requests
import base64
import base64
import magic
import io
import mimetypes
import codecs

from typing import Union, List
from fastapi import FastAPI, File, UploadFile, Request, Form
from crawler import crawler

client = crawler()
app = FastAPI()
sessionr = requests.session()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post('/addcookies/')
async def receive_cookies(request: Request):
    cookies = await request.json()
    requests.utils.add_dict_to_cookiejar(sessionr.cookies, cookies)
    return sessionr.cookies

# from typing import List
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str

# class ItemList(BaseModel):
#     items: List[Item]
#     processo: str,
#     tipo: str
    
### ARRUMAR OS PONTOS DO PROCESSO
@app.post("/upload")
async def upload(request: Request):
    form = await request.json()
    # filename =  form['files'].filename
    tipo = form['tipo']
    files = form['files']
    for file in files:
        mime, mimetype = get_extension(file)
        file = base64.b64decode(file)
        parametro = client.find_text(tipo)
        html = client.buscar_links(numero_processo=form['processo'], session=sessionr, num_termo=parametro)
        prepare = client.upload_file(peticionarHTML=html, session=sessionr, num_termo=parametro)
        client.requisoes_upload(filename=filename, payload_init=self.payload_init, headers_init=self.headers_init, peticionarHTML=peticionarHTML, cid=cid, session=session, num_termo=num_termo, file=file, qtdDoc=qtdDoc, ViewState=ViewState)
    

    # except Exception:
    #     return {"message": "There was an error uploading the file"}
    
    return {"message": f"Successfully uploaded {filename}"}





#   Utils
###################################################################
def get_extension(str_base64):
    bytesData = io.BytesIO()
    bytesData.write(base64.b64decode(str_base64))
    bytesData.seek(0)
    mime = magic.from_buffer(bytesData.read(), mime=True)
    mimetype = mimetypes.guess_extension(mime)
    return mime, mimetype

def get_content(required_fields):
    content = Request.json()
    validate_content(content, required_fields)
    return content

def validate_content(content, required_fields):
    for field in required_fields:
        if field not in content:
            raise print("Requisição inválida.")

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