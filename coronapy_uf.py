import requests
import json
import pandas as pd

# Emulando uma requisição ao site, baseado na inspeção do pacotes enviados ao servidor
headers = {
    'authority': 'xx9p7hp1p7.execute-api.us-east-1.amazonaws.com',
    'accept': 'application/json, text/plain, */*',
    'sec-fetch-dest': 'empty',
    'x-parse-application-id': 'unAFkcaNDeXajurGB7LChj8SgQYS2ptm',
    'origin': 'https://covid.saude.gov.br',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://covid.saude.gov.br/',
    'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
}
total = requests.get('https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalAcumulo', headers=headers)
mapa = requests.get('https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalMapa', headers=headers)

# Transformando tudo em json, para ficar mais fácil de manipular depois
total = json.loads(total.content)['results']
mapa = json.loads(mapa.content)['results']

# Tirando algumas colunas indesejadas
ufs = pd.DataFrame(mapa)
ufs = ufs.drop(['objectId', 'latitude', 'longitude', 'createdAt', 'percent'], axis=1)
print("#"*10 + " INFORME O CÓDIGO DO ESTADO CONFORME TABELA ABAIXO " + "#"*10)
print(" ")
print(ufs.nome)
print(" ")
print("#"*100)
print(" ")
estado_informado = input("INFORME O CÓDIGO: ")
print(" ")
print("#"*100)
if estado_informado == "":
    print(" ")
    print ("CÓDIGO INFORMADO É INVÁLIDO!")
    print ("CÓDIGO AUTOMATICAMENTE ALTERADO PARA 25 (SP)")
    print(" ")
else:
    print(" ")
    print("ESTADO:               " + str(ufs.nome[int(estado_informado)]))
    print("CASOS CONFIRMADOS:    " + str(ufs.qtd_confirmado[int(estado_informado)]))
    print("ÓBITOS:               " + str(ufs.qtd_obito[int(estado_informado)]))
    print("TX LETALIDADE (%):    " + str(ufs.letalidade[int(estado_informado)]))
    print(" ")
    print("#"*100)
