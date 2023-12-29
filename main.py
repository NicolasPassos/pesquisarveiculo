from fastapi import FastAPI
from routes.carro_route import *
import uvicorn

class Server():
    def __init__(self) -> None:
        self.api = FastAPI(title='PYGEN')
        self.api.include_router(carro_route)
        uvicorn.run(self.api, port=8080, host='0.0.0.0')


if __name__ == '__main__':
    api = Server()