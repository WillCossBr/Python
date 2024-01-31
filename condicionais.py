#Condicionais
#Existem três tipos de condicionais, são eles:
#. Simples
#. Composto
#. Encadeado

#----------------------------------------------------------------
#Condicional Simples - if

print("Condicional Simples - if")
print("""Faça um programa que calcula a média do aluno
e veja se ele foi aprovado ou não. O valor necessário
para passar é de 70%.""")
print('-'*30)

#variaveis
prova1 = ""
prova2 = ""
media = 0.00

#entradas
print("Digite a nota da primeira prova: ")
prova1 = float(input())

print("Digite a nota da segunda prova: ")
prova2 = float(input())

print('\n')

#processamento
media = ((prova1 + prova2) / 2)

#saidas
if media > 69:
    print("Parabéns você foi aprovado! Sua média é de: ", media,"%")

if media  < 70:
    print("Tente novamente, você foi reprovado! Sua média é de: ", media,"%")

print('-'*30)

#----------------------------------------------------------------
#Condicional Composta - if / else
#Mesmo exercício, porém resolvido com condicional composta

print("Condicional Composta - if / else")
print("""Faça um programa que calcula a média do aluno
e veja se ele foi aprovado ou não. O valor necessário
para passar é de 70%.""")
print('-'*30)

#variaveis
prova1 = ""
prova2 = ""
media = 0.00

#entradas
print("Digite a nota da primeira prova: ")
prova1 = float(input())

print("Digite a nota da segunda prova: ")
prova2 = float(input())

print('\n')

#processamento
media = ((prova1 + prova2) / 2)

#saidas
if media > 69:
    print("Parabéns você foi aprovado! Sua média é de: ", media,"%")

else:
    print("Tente novamente, você foi reprovado! Sua média é de: ", media,"%")

print('-'*30)

#----------------------------------------------------------------
#Condicional Encadeado - elif

print("Condicional Encadeado - elif")
print("""Faça um programa que calcula a média do aluno
e veja se ele foi aprovado, ficou de recuperação ou foi reprovado.
Os valores são:
70% até 100% -> aprovado!
50% até 69%  -> recuperação!
0% até 49%   -> reprovado!""")
print('-'*30)

#variaveis
x1 = ""
x2 = ""
x3 = ""

#entradas
print("Digite a nota da primeira prova: ")
x1 = float(input())

print("Digite a nota da segunda prova: ")
x2 = float(input())

#processamento
x3 = ((x1 + x2) / 2)

#elif funciona como um switch case de outras linguagens de programação.
#saidas
if (x3 >= 0) and (x3 <= 49):
    print("Tente novamente, você foi reprovado! Sua média é de: ", x3,"%")
elif (x3 >= 50) and (x3 <= 69):
    print("Se esforce mais, você ficou de recuperação! Sua média é de: ", x3,"%")
else:
    print("Parabéns você foi aprovado! Sua média é de: ", x3,"%")

print('-'*30)

#----------------------------------------------------------------
