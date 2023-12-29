from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import requests
from bs4 import BeautifulSoup
from lxml import etree

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
    link = 'Não Disponível'
    content_html = BeautifulSoup(response.content,'html.parser')
    info_carro = content_html.find_all('dl',attrs={"class":"dl-horizontal"})
    for i in info_carro[0].contents:
        if '\n' in i:
            continue
    #try:
    #    if 'Marca' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[1]')[0].text:
    #        marca = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[1]/text()')[0]
#
    #    nome = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[2]/h1/text()')[0]
#
    #    if 'Ano' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[2]')[0].text:
    #        ano = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[2]/text()')[0]
#
    #    if 'Cor' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[3]')[0].text:
    #        cor = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[3]/text()')[0]
    #    
    #    if 'Motor' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[4]')[0].text:
    #        motorizacao = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[4]/text()')[0]
    #    
    #    if 'Km' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[5]')[0].text:
    #        km = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[5]/text()')[0]
#
    #    if 'Comb' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[6]')[0].text:
    #        combustivel = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[6]/text()')[0]
#
    #    if 'Ítens' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[7]')[0].text: 
    #        itens = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[7]/text()')[0]
    #    
    #    if 'Obs' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[8]')[0].text:
    #        observacao = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[8]/text()')[0]
    #    
    #    if 'Cidade' in tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dt[9]')[0].text:
    #        cidade = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[9]/text()')[0]
    #    
    #    preco = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/div[1]/span')[0].text
#
    #except:
    #    pass
    carro = Carro(marca=marca,
                  nome=nome,
                  ano=ano,
                  cor=cor,
                  motorizacao=motorizacao,
                  km=km,
                  combustivel=combustivel,
                  itens=itens,
                  observacao=observacao,
                  cidade=cidade,
                  preco=preco,
                  link=link)
    return carro


def pesquisar_carro(carro):
    navegador = webdriver.Chrome()

    navegador.get('https://www.usadofacil.com.br/V6/default.asp')
    navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[1]/div/form/div[2]/input').send_keys(f'{carro}')
    navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[1]/div/form/div[3]/div/select/option[23]').click()
    navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[1]/div/form/div[6]/div/select/option[28]').click()
    navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[1]/div/form/button').submit()

    links_carros = []
    carros = []

    while navegador.find_element(By.CSS_SELECTOR,'strong').text != navegador.find_element(By.CSS_SELECTOR,'strong+ strong').text:
        links = navegador.find_elements(By.CSS_SELECTOR,'.panel-heading')
        for i in links:
            link = i.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
            links_carros.append(link)
        botoes = navegador.find_elements(By.CSS_SELECTOR,'.tamanho-botao')
        for botao in botoes:
            if 'Próximo' in botao.accessible_name:
                botao.submit()
            if len(botoes) == 1 and 'Próximo' not in botao.accessible_name:
                logging.info('Acabaram as páginas.')
    for i in links_carros:
        detalhe = buscar_detalhes(i)
        carros.append(detalhe)
    
    return carros

a = buscar_detalhes('https://www.usadofacil.com.br/V6/detalhes.asp?cod=1129852&an=658&veiculo=onix-joy-flex-mecanico')
print(a)
