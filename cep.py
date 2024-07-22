import requests

#Inform the
cep = input('Digite seu CEP ')
#include my input in the url with the values ​​informed by the client.
url = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(url)
if response.status_code == 200:
    meuaquivo = response.json()
    #accessing the API information, and showing the relevant files.
    print(f"Seu Cep é: {meuaquivo['cep']}")
    print(f"RUA: {meuaquivo['logradouro']}")
    print(f"Bairro: {meuaquivo['bairro']}")
    print(f"Municipio: {meuaquivo['localidade']}")
    print(f"Estado: {meuaquivo['uf']}")
else:
    #error in the request, anything that is not coigo 200.
    print('Falha na solicitação')



