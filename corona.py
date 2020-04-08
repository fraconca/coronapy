import requests
import json
import pandas as pd

#Coletando Headers
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

# Request da API com GET
total = requests.get('https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalAcumulo', headers=headers)
mapa = requests.get('https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalMapa', headers=headers)

# Transformando tudo em json, para ficar mais fácil de manipular depois
total = json.loads(total.content)['results']
mapa = json.loads(mapa.content)['results']

# Formatando dados dos estados (ufs) com Pandas DataFrame
ufs = pd.DataFrame(mapa)
ufs = ufs.drop(['objectId', 'latitude', 'longitude', 'createdAt', 'updatedAt', 'percent'], axis=1)

# Acessa o último caso registrado
# print(total[-1])

# Percorrendo array multidimencional para leitura de dados
covid_casos_br = total[-1]["qtd_confirmado"]
covid_obitos_br = total[-1]["qtd_obito"]

# Inicia Cálculo de Percentual de Casos e Mortes
# População Brasileira Segundo Dados do PNAD
# https://educa.ibge.gov.br/jovens/conheca-o-brasil/populacao/18320-quantidade-de-homens-e-mulheres.html
populacao_br_pnad = 211355320

# Calcular Percentual de Casos x Mortes
populacao_br_pct_casos = covid_casos_br/populacao_br_pnad
populacao_br_pct_mortes = covid_obitos_br/populacao_br_pnad

# Converte formato em Percentual e aumenta 4 casas decimais
populacao_br_pct_casos_f = "{:.4%}".format(populacao_br_pct_casos)
populacao_br_pct_mortes_f = "{:.4%}".format(populacao_br_pct_mortes)

#Print dos dados
print("#"*62)
print(" ")
print(" TOTAL DE CASOS:                                      " + str(covid_casos_br))
print(" % DE CASOS:                                          " + str(populacao_br_pct_casos_f))
print(" ")
print(" TOTAL DE ÓBITOS:                                     " + str(covid_obitos_br))
print(" % DE ÓBITOS:                                         " + str(populacao_br_pct_mortes_f))
print(" ")
print("#"*62)
print(ufs)
print("#"*62)
