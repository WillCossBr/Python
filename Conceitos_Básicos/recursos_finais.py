#----------------------------------------------------------------
#Trocar valores entre duas variáveis:

print(30*'-')
print('Trocar valores de duas variáveis:')
print('\n')

#criação das variáveis
var1 = 12
var2 = 31

print('Variáveis antes da troca: ')
print(f'var1: {var1}, var2: {var2}')
print('\n')

#troca de valores
var2, var1 = var1, var2

print('Variáveis depois da troca: ')
print(f'var1: {var1}, var2: {var2}')
print('-'*30)

#----------------------------------------------------------------
#Operador ternário:

print('Operador ternário: ')
print('\n')
print('Verifica qual variável é menor: ')

menor = var1 if var1 < var2 else var2
print(f'Menor valor: {menor}')
print('\n')
print('Usando tuplas: ')
print(f'Menor valor: {(var2, var2)[var1 < var2]}')
print('-'*30)

#----------------------------------------------------------------
#Generators

valores = [1,3,5,7,9,11,13,15]
quadrados = (item**2 for item in valores)
print(quadrados)
for valor in quadrados:
    print(valor)

print('-'*30)

#----------------------------------------------------------------
#Função enumerate()

print('Função enumerate: ')
print('Retorna o índice e o conteúdo: ')
print('\n')

bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Índice: {i} Item: {item}')

print(30*'-')

#----------------------------------------------------------------

temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t}ºC.')

print('-'*30)

#----------------------------------------------------------------
#abrir arquivo normalmente:

print('abrir arquivo: ')
try:
    a = open('arq.txt', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    a.close()

print('-'*30)

#Gerenciamento de contexto com with
print('abrir arquivo com gerenciamento de contexto: ')
with open('arq.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha)

#----------------------------------------------------------------
