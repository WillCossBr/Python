#----------------------------------------------------------------
#Números Aleatórios

#gerando um número aleatório
import random

valor = random.randint(1,20)
print(valor)

#----------------------------------------------------------------
#Números Aleatórios com o laço for

print('-'*30)
print("gerar 5 números aleatórios entre 1 e 50: \n")

# laço
# i = variável criado para iterar o laço for
# laço se repete 5 vezes
for i in range(5):
    # n = variável criado para receber os números aleatórios
    # random.randint() = função que cria os números aleatórios(inteiros)
    n = random.randint(1,50)
    print(f'Número gerado: {n}')

print('-'*30)

#----------------------------------------------------------------
#Números aleatórios de ponto flutuante (float)

print('Gerar um número aleatório float entre 0 e 1')

#random.random = gera um número float aleatório entre 0 e 1 ex: 0,5698....
#não aceita parametros 
numero = random.random()
print(numero)

print('-'*30)

#----------------------------------------------------------------
#Números aleatórios de ponto flutuante (float) entre 0 e 10

print('Gerar um número aleatório float entre 0 e 10')

#random.random = gera um número float aleatório entre 0 e 10
#não aceita parametros 
numero = random.random()
#multiplicamos o valor por 10
print(f'Número gerado: {numero * 10}')

print('-'*30)

#----------------------------------------------------------------

#obs: como a função ramdom.ramdom() gera números aleatórios apenas
#entre 0 e 1, para podermos aumentarmos essa escala multiplicamos
#a variável pelo tamanho da escala desejada.
#ex float randômicos entre 0 e 10 = variável * 10
#ex float randômicos entre 0 e 100 = variável * 100
#ex float randômicos entre 0 e 99999 = variável * 99999

#----------------------------------------------------------------
#Arredondamento de números aleatórios

x = random.random()

print(f'Número antes do arrendomento: {x}\n')

#round(variável, 2) = arredonda o número duas casas decimais
print(f'Número depois do arrendomento: {round(x,2)}')

print('-'*30)

#----------------------------------------------------------------
#Números aleatórios de ponto flutuante (float) gerados pelo método uniform:

print('Randômicos floats entre (1,100) pelo método uniform: \n')

x1 = random.uniform(1,100)
print(f'Número: {x1}')
print("-"*30)
#Neste caso eu não preciso multiplicar o número, pois o método aceita parametros

#----------------------------------------------------------------
#Números aleatórios gerado pelo método random.choice:
#funciona sorteando números de uma lista de forma aleatória.
#choice = escolha

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

x3 = random.choice(lista)

print('Aleatórios sorteados pelo método random.choice()')
print(lista)
print(f'Número escolhido: {x3}')
print('-'*30)

#----------------------------------------------------------------
#Números aleatórios gerado pelo método random.sample:
#sample = amostra

print('Aleatórios pelo método random.sample: (amostra)')
x4 = random.sample(lista,5)

print(f'Amostra de números: {x4}')
print('-'*30)

#----------------------------------------------------------------
#Embaralhar lista

print('Embaralhar listas:')
print(f'Exibir lista original: {lista}')

#embaralha a lista
x5 = random.shuffle(lista)

print(f'Exibir lista embaralhada: {lista}')
print('-'*30)

#----------------------------------------------------------------
