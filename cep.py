import requests
#criar um programa que acesse o CEP


cep = input('Digite seu CEP ')
#Acessar a API que fornecer os CEP.
#include my input in the url with the values ​​informed by the client.
url = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(url)
if response.status_code == 200:
    meuaquivo = response.json()
    print(f"Seu Cep é: {meuaquivo['cep']}")
    print(f"RUA: {meuaquivo['logradouro']}")
    print(f"Bairro: {meuaquivo['bairro']}")
    print(f"Municipio: {meuaquivo['localidade']}")
    print(f"Estado: {meuaquivo['uf']}")
else:
    print('Falha na solicitação')



