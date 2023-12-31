from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import requests
from bs4 import BeautifulSoup
from lxml import etree
import urllib.parse

class Carro:
    def __init__(self,marca: str,nome: str,ano: str,cor: str,motorizacao: str,km: str,combustivel: str,itens: str,observacao: str,cidade: str,preco: str,link: str =None):
        self.marca = marca
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.motorizacao = motorizacao
        self.km = km
        self.combustivel = combustivel
        self.itens = itens
        self.observacao = observacao
        self.cidade = cidade
        self.preco = preco
        self.link = link

def buscar_detalhes(link: str):
    try:
        response = requests.get(url=link, verify=False)
        marca = 'Não Disponível'
        nome = 'Não Disponível'
        ano = 'Não Disponível'
        cor = 'Não Disponível'
        motorizacao = 'Não Disponível'
        km = 'Não Disponível'
        combustivel = 'Não Disponível'
        itens = 'Não Disponível'
        observacao = 'Não Disponível'
        cidade = 'Não Disponível'
        preco = 'Não Disponível'

        content_html = BeautifulSoup(response.content,'html.parser')
        nome = content_html.find_all('h1',attrs={"class":"title-item"})[0].text
        preco = content_html.find_all('div',attrs={"class":"preco"})[0].contents[1].text
        info_carro = content_html.find_all('dl',attrs={"class":"dl-horizontal"})
        detalhes_carro = info_carro[0].contents
        detalhes_carro = [info.text for info in detalhes_carro if info != '\n']
        for index,item in enumerate(detalhes_carro):
            if 'marca' in item.lower():
                marca = detalhes_carro[index+1]
            elif 'ano' in item.lower():
                ano = detalhes_carro[index+1]
            elif 'cor' in item.lower():
                cor = detalhes_carro[index+1]
            elif 'motor' in item.lower():
                motorizacao = detalhes_carro[index+1]
            elif 'km' in item.lower():
                km = detalhes_carro[index+1]
            elif 'comb' in item.lower():
                combustivel = detalhes_carro[index+1]
            elif 'ítens' in item.lower():
                itens = detalhes_carro[index+1]
            elif 'obs' in item.lower():
                observacao = detalhes_carro[index+1]
            elif 'cidade' in item.lower():
                cidade = detalhes_carro[index+1]

        carro = Carro(marca=marca.capitalize(),
                    nome=nome,
                    ano=ano,
                    cor=cor,
                    motorizacao=motorizacao,
                    km=km,
                    combustivel=combustivel,
                    itens=itens,
                    observacao=observacao.capitalize(),
                    cidade=cidade,
                    preco=preco,
                    link=link)
        return carro.__dict__
    except Exception as e:
        raise Exception(f'Houve um erro no site da Usado Fácil: {e}')

def pesquisar_carro(carro,valor_medio='',ano='',motorizacao='',cidade='',marca=''):
    links_carros = []
    dados_carros = []
    resultado = 'Não foram encontrados carros com esta nomenclatura.'
    try:
        pagina_atual = 0
        url_busca_inicial = f'https://www.usadofacil.com.br/comprar-0/veiculo-{carro}/ano-{ano}/valor-{valor_medio}/cidade-{cidade}/motorizacao-{motorizacao}/default/'
        response = requests.get(url_busca_inicial)
        content_html = BeautifulSoup(response.content,'html.parser')
        carros = content_html.find_all('div',attrs={"class":"panel panel-default panel-lista"})
        if len(carros) >= 1:
            total_paginas = int(content_html.find_all('p',attrs={"class":"contador-pag"})[0].contents[3].text)
            cidade_formatada = urllib.parse.quote(cidade)
            while pagina_atual != total_paginas:
                url_busca_all = "https://www.usadofacil.com.br/V6/resultado.asp"
                header = {'authority': 'www.usadofacil.com.br',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'origin': 'https://www.usadofacil.com.br',
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': f'https://www.usadofacil.com.br/veiculo-{carro}/ano-{ano}/valor-{valor_medio}/motorizacao-{motorizacao}/comum/'}
                
                payload = f'CurrentPage={pagina_atual}&veiculo={carro}&valor={valor_medio}&ano={ano}&motorizacao={motorizacao}&cidade={cidade_formatada}&tipo=&origem=comum&ar=&dh=&tr=&ve=&ca=&combustivel=&marca={marca}&filtro-ano=&filtro-valor=&filtro-motor=&filtro-cor-preto=&filtro-cor-cinza=&filtro-cor-prata=&filtro-cor-branco=&filtro-cor-vermelho=&filtro-cor-laranja=&filtro-cor-amarelo=&filtro-cor-marrom=&filtro-cor-azul=&filtro-cor-verde=&filtro-cor-outras=&filtro-ar=&filtro-ve=&filtro-te=&filtro-dh=&filtro-de=&filtro-ca=&Proximo=Pr%C3%B3ximo%20%E2%86%92'
                response = requests.post(url_busca_all,data=payload, headers=header)
                content_html = BeautifulSoup(response.content,'html.parser')
                carros = content_html.find_all('div',attrs={"class":"panel panel-default panel-lista"})
                for i in carros:
                    link = i.find_all('a')[0].attrs['href']
                    link = 'https://www.usadofacil.com.br/V6/' + link
                    links_carros.append(link)
                
                pagina_atual += 1

            for i in links_carros:
                detalhe = buscar_detalhes(i)
                dados_carros.append(detalhe)
                resultado = f'Foram encontrados os seguintes dados'
    except Exception as e:
        raise Exception(f'Houve um erro no site da Usado Fácil: {e}')
    
    return resultado,dados_carros