#escrever arquivos em json:

print(30*'-')
print('Escrever em arquivos json: ')

#importa o módulo
import json

#dados que deseja escrever
dados = {
    "nome": "Danones.LTDA",
    "telefone": "(55) 3333-3333",
    "email": "danones.ltda@gmail.com",
    "endereco": "Rua do limoeiro, 123, Bairro: Monica",
}

#endereço do arquivo que deseja editar
local = "/home/william/Python/Manipula_Arqs/Json/fornecedores.json"

#editar o arquivo:
with open(local, 'w') as fornecedores:
    json.dump(dados, fornecedores)

#Confirmação de deu certo!
print('Dados inseridos com sucesso!')

print(30*'-')

#impressão do arquivo:
with open(local, 'r') as fornecedores:
    leitor = json.load(fornecedores)
    print(json.dumps(leitor ,indent=4))


print('-'*30)
