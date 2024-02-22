#----------------------------------------------------------------
#Listas
#representa uma sequência de valores do mesmo tipo
#Sintaxe: nome-lista = [valores]
#exemplo - 1:

print('-'*30)
notas = [5,7,8,6,9]
print(f'Lista de notas: {notas}')
print('-'*30)

#----------------------------------------------------------------
#listas concatenadas

print('Listas concatenadas')

lista_letras = ["a","b","c","d","e"]
lista_numeros = [1,2,3,4,5]
lista_concatenada = lista_letras + lista_numeros

print(f'Lista de letras: {lista_letras}')
print(f'Lista de números: {lista_numeros}')
print(f'Soma de duas listas: {lista_concatenada}')
print('-'*30)

#----------------------------------------------------------------
#acessar as posições da lista

print('acessar as posições da lista')
print(f'lista de letras: {lista_letras}')
print('lista_letras[4]')
print(f'Acessar a quarta posição da lista: {lista_letras[4]}')
print('-'*30)

#----------------------------------------------------------------
#atribuir novo valor para posições da lista

lista_letras[4] = "abcd"
print('alterar valores dentro da lista')
print(f'lista de letras: {lista_letras}')
print('lista_letras[4] = adcd')
print('-'*30)

#----------------------------------------------------------------
#acessar um pedaço da lista

print('acessar um pedaço da lista')
print(f'lista de letras: {lista_letras}')
print('lista_letras[0:3] = [a,b,c]')
print(lista_letras[0:3])
print('-'*30)

#----------------------------------------------------------------
# saber o tamanho da lista

print('saber o tamanho da lista')
print(f'(len(lista_letras))')
print(f'tamanho da lista: {(len(lista_letras))}')
print('-'*30)

#----------------------------------------------------------------
# somar os valores da lista

print('somar os valores da lista:')
print(f'(sum(lista_numeros))')
print(lista_numeros)
print(sum(lista_numeros))
print('-'*30)

#----------------------------------------------------------------
# valor minimo e máximo da lista

print('valor minino e máximo da lista:')
print(f'(min(lista_numeros))(max(lista_numeros))')
print(lista_numeros)
print(min(lista_numeros))
print(max(lista_numeros))
print('-'*30)

#----------------------------------------------------------------
# inserir um novo elemento ao final da lista:

print('inserir um elemento no final da lista:')
print(f'(lista_numeros.append(x))') #x = valor a ser acrescentado
print(lista_numeros)
lista_numeros.append(999)
print(lista_numeros)
print('-'*30)

#lista.insert(3,21) insere um número (21) numa posição específica da lista(3)

#----------------------------------------------------------------
# retirar o ultimo elemento do final da lista:

print('retirar um elemento do final da lista:')
print(f'(lista_numeros.pop()') #x = valor a ser acrescentado
print(lista_numeros)
lista_numeros.pop()
print(lista_numeros)
print('-'*30)

# Se quiser tirar um elemento específico, basta colocar o número
#da posição que deseja retirar ex...lista.pop(3)

# print(12 in lista) = itera a lista procurando o valor 12

#----------------------------------------------------------------
# iterar a lista com o laço for:

lista_planetas = ["Mercúrio", "Vênus", "Marte", "Saturno", "Urano", "Netuno"]

print('Iterar a lista com o laço for')
#laço
for planetas in lista_planetas:
    print(planetas)

print('-'*30)

#----------------------------------------------------------------
# exercício:
print('Exercício:\n')
print('''Crie um script que peça para o usuário digitar o nome de cinco bebidas
favoritas dele, armazenando esses valores em uma lista.
    Na sequência, exiba na tela os elementos da lista em ordem alfabética,
uma por linha, usando um laço de repetição for.\n''')

#variáveis
lista_bebidas = []
j = 1
resposta = ""

#entrada
print('-'*30)
print("Lista da sua cinco bebidas favoritas: ")

for i in range(5):
    (print(f'{j}º bebida: '))
    resposta = input()
    lista_bebidas.append(resposta)
    print('\n')
    j += 1
print('-'*30)

#processamento
lista_bebidas.sort()

#saida
cont = 0

print('Lista das bebidas: ')
for i in range(5):
    print(lista_bebidas[cont])
    cont += 1
print('-'*30)

#----------------------------------------------------------------
