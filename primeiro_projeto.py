import requests

#Cabecario

def main():

    print('### API Via CEP ###')

#pedindo informação do usiario 



cep_input = input("digite o CEP para consulta: ")
while len(cep_input) !=8:
    print("CEP informado está invalido: ")
    cep_input = input("informe o CEP valido: ")
    
    exit()
    print("resultado da consulta: ")

#fazendo a requisição

request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

adress_data = request.json()

if 'erro' not in adress_data:
    print('CEP: {}' .format(adress_data['cep']))
    print('rua/avenida: {}' .format(adress_data['logradouro']))
    print('Complemento: {}' .format(adress_data['complemento']))
    print('Bairro: {}' .format(adress_data['bairro']))
    print('Cidade: {}' .format(adress_data['localidade']))
    print('Estado: {}' .format(adress_data['uf']))

else:
    print('{}:cep INVALIDO. '.format(cep_input))
    print('--------------------------------------------------------------------------------')

option = int(input('deseja realizar outra busca?\n 1- sim \n 2- sair \n:'))

if option == 1 :
    main()
else:
    print('saindo...')

#nome do ambiente de nivel superior do programa
if __name__ == 'main':
    main()
