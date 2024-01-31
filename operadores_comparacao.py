#----------------------------------------------------------------
#Operadores de Comparação

# igual - ==
# diferente !=
# maior - >
# menor - <
# maior ou igual - >=
# menor ou igual - <=

#----------------------------------------------------------------
#Ordem de precedência
# 1º operadores aritméticos
# 2º operadores comparativos

#Operadores de comparação sempre retornarão: TRUE ou FALSE

#Exemplo - 1
a = 5
b = 5

print("-"*30)
print("Exemplo - 1")
print(b != a + 1)
#a + 1 = 6
#b != 6 = True

print(a * 2 >= b)
#a * 2 = 10
#10 >= b = True
print("-"*30)

#----------------------------------------------------------------
#Exemplo - 2
print("Exemplo - 2")

x = False
y = False
z = False
n1 = 0
n2 = 0

#entradas
print("Digite um número: ")
n1 = int(input())

print("Digite um número: ")
n2 = int(input())

#processamento
x  = n1 == n2

print('\n')

#saida
print('São iguais?', x)

#processamento
z = n1 > n2

#saida
print(n1,"é maior que", n2, "?", z,)

#processamento
y = n1 != n2

#saida
#casting = para concatenar o valor de y boleano
#primeiro converta-o para string = str(y)
print("Sao Diferentes? " + str(y))

print('-'*30)