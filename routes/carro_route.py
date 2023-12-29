from fastapi import APIRouter, status, Response, Header
from models.response_models import *
import io
from repositories.carro import pesquisar_carro

carro_route = APIRouter()

@carro_route.get("/buscarcarros/{carro}")
def getcarro(carro: str):
    try:
        pesquisa = pesquisar_carro(carro)

        return pesquisa
    except Exception as e:
        return ResponseModel(Message=f'Achei não bói',
                          Status_code=404,
                          Detail='Achei não bói',
                          Response=None)