#----------------------------------------------------------------
#dicionários:

elemento = {
    "Z": 3,
    "nome": "Lítio",
    "grupo": "Metais Alcalinos",
    "densidade": 0.534
}

print(f'elemento: {elemento["nome"]}')
print(f'Densidade: {elemento["densidade"]}')
print(f'O Dicionário possui {len(elemento)} elementos.')
print('\n')
print('-'*30)

#----------------------------------------------------------------
#Atualizar uma entrada no dicionário:
print('Atualizar uma entrada  no dicionário')
elemento['grupo'] = 'Alcalinos'
print(elemento)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#adicionar uma entrada:

print('Adicionar uma entrada: ')
elemento['período'] = 1
print(elemento)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#excluir itens do dicionário:

print('excluir itens do dicionário: ')
del elemento['período']
print(elemento)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#limpar o dicionario:

print('limpar dicionário: ')
elemento.clear()
print(elemento)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#excluir o dicionario:

print('excluir o dicionário: ')
del elemento
print('\n')
print('-'*30)

#----------------------------------------------------------------
#métodos:

cliente = {
    'Nome': 'joão',
    'idade': 30,
    'sexo': 'M',
    'salário': 1500.00 
}

#exibe os itens do dicionário: items()
print('exibir dicionario: cliente')
print(cliente.items())
print('\n')
print('-'*30)

#----------------------------------------------------------------
#exibe somente as chaves do dicionário: keys()

print('exibe somente as chaves do dicionário: ')
print(cliente.keys())
print('\n')
print('-'*30)

#----------------------------------------------------------------
#exibe somente os valores do dicionário: values()

print('exibe somente as chaves do dicionário: ')
print(cliente.values())
print('\n')
print('-'*30)

#----------------------------------------------------------------
#desempacotar as chaves e valores simultaneamente:

print('chaves e valores simultâneos: (tabela)')
for i,j in cliente.items():
    print(f'{i}: {j}')

print('\n')
print('-'*30)

#----------------------------------------------------------------
