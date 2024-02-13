#----------------------------------------------------------------
#Funções lambda (anônimas)
#lambdas são funções curtas que você cria em uma
#única linha e pode atribui-las a uma variável.
# sintaxe:
# lambda argumentos: expressão
#exemplo - 1, calcula o quadrado de um número

quadrado = lambda x: x**2

print('-'*30)
print("Calcula quadrado: ")
for i in range(1, 11):
    print(quadrado(i))

print('-'*30)

#----------------------------------------------------------------
#exemplo - 2, verifica se o número é par

print("Verifica se o número é par: ")
par = lambda y: y % 2 == 0
print(par(10))

print('-'*30)

#----------------------------------------------------------------
#exemplo - 3, converte fahrenheit para celsius

print('Converte fahrenheit para celsius: ')
f_c = lambda f: (f - 32) * 5/9
print(f_c(32))

print('-'*30)

#----------------------------------------------------------------
#exemplo - 4, Função map()
#sintaxe:
# map(função, iterável)

print("Multiplica por 2: ")
lista = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x * 2, lista))
print(dobro)

print('-'*30)

#----------------------------------------------------------------
#exemplo - 5, função map, convertendo letras maiusculas 

print("Converção de letras para maiusculas: ")
palavras = ["Python", "é", "uma", "linguagem", "de", "programação"]
maiusculas = list(map(str.upper, palavras))
print(maiusculas)

print('-'*30)

#----------------------------------------------------------------
#exemplo - 6, Função filter()
#itera a lista e devolve uma lista de valores
#valores que derem resultado True

#sintaxe:
#filter(função, sequência)

print("Extrair números pares: ")

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num_par = list(filter(numeros_pares, numeros))
print(num_par)

print('-'*30)

#----------------------------------------------------------------

print("Extrair números ímpares: ")

x1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num_impar = list(filter(lambda x: x % 2 != 0, x1))
print(num_impar)

print('-'*30)

#----------------------------------------------------------------
#Função reduce()
#realiza operações cumulativas e retorna
#um único valor no final

#sintaxe:
#reduce(função, sequência, valor_inicial)

print("Realiza operações cumulativas com reduce(): ")
from functools import reduce

def mult(a, b):
    return a*b

lista_numeros = [1,2,3,4,5,6]

total = reduce(mult, lista_numeros)
print(total)

print('-'*30)

#----------------------------------------------------------------
#soma cumulativa dos quadrados de valores
#usando expressão lambda

print("Soma cumulativa dos quadrados dos valores: ")

list_num = [1,2,3,4]

#((1² + 2²)² + 3²)² + 4²

total1 = reduce(lambda x, y: x**2 + y**2, list_num)
print(total1)

print('-'*30)

#----------------------------------------------------------------
