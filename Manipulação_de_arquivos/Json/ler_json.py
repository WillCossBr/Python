# Json (JavaScript Object Notation) é um formato
# de dados leve e independente. Usado para armazenar
# e trocar dados entre servidor e cliente. Fácil de ler
# e escrever para humanos e fácil de analisar e gerar
# para máquinas.
# Permite serialização e desserialização.

# CARACTERÍSTICAS:
# estrutura simples
# suporte a vários tipos de dados
# leve e legível

print(30*'-')
print('Abrir um arquivo em Json: ')
print('\n')

#importe o módulo
import json

#variavel com o caminho do arquivo
endereço = "/home/william/Python/Manipula_Arqs/clientes.json"

#with = abre e fecha o arquivo
#open = ('caminho' + modo(leitura=r, ou escrita=w))
#as = apelido doa rquivo
with open(endereço,'r',encoding='utf-8') as clientes:

    #cria uma variavel para receber o arquivo importado
    leitor = json.load(clientes)

    #imprime o arquivo
    #json.dumps, indent = identa e organiza o arquivo para sua exibição
    print(json.dumps(leitor ,indent=4))

print(30*'-')
