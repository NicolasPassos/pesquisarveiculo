import requests
from bs4 import BeautifulSoup
from lxml import etree
response = requests.get('https://www.usadofacil.com.br/V6/detalhes.asp?cod=1125923&an=85&veiculo=etios-hatch-x-flex-mecanico', verify=False)
content_html = BeautifulSoup(response.content,'html.parser')
content_html = str(content_html)
#Parsing do HTML com o lxml
parser = etree.HTMLParser()
tree = etree.fromstring(content_html, parser)
#Busca do elemento com o XPath
marca = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[1]/text()')[0]
ano = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[2]/text()')[0]
cor = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[3]/text()')[0]
motor = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[4]/text()')[0]
km = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[5]/text()')[0]
combustivel = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[6]/text()')[0]
itens = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[7]/text()')[0]
observacao = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[8]/text()')[0]
cidade = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/dl/dd[9]/text()')[0]
preco = tree.xpath('/html/body/div[1]/div/div[3]/main/div[2]/div[1]/div[1]/div[4]/div/div[1]/span')[0].text

print(authenticity_token)