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
# total = json.loads(total.content)['results']
mapa = json.loads(mapa.content)['results']

print(mapa)
