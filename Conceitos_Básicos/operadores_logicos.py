#Operadores lógicos

# AND = ambas entradas verdadeiras
# OR = apenas uma entrada verdadeira
# NOT = inverte a entrada

#----------------------------------------------------------------
# Exemplo 1 END

print('-'*30)
print('Exemplo - 1 END')
print('''Para entrar no parque de diversão as pessoas precisam ter
no minimo 18 anos e altura minima de 1,60m. Faça um algoritmo que
faça esse cálculo e diga se a pessoa pode entrar ou não.''')
print('-'*30)

#variaveis
idade = ""
altura = ""
resultado = ""

#entradas
print("PARQUE DE DIVERSÃO")

print("Digite sua idade: ")
idade = int(input())

print("Digite sua altura: ")
altura = float(input())

#processamento
resultado = (idade >= 18) and (altura >= 1.60)

#saidas
if resultado == True:
    print("Seja bem vindo!")

else:
    print("Acesso Negado!")

print('-'*30)

#----------------------------------------------------------------
# Exemplo 2 OR

print('Exemplo - 2 OR')
print('''O sistema de alarme de um estabelecimento pequeno, possui um
alarme voltado para sua janela e outro para a porta. Os dois alarmes
detectam o travamento de ambas. Faça um algoritmo que dispare um alarme
caso a porta ou a janela seje aberta.''')


#variáveis
# f = fechada
# a = aberta
# A entrada seria detectada por um sensor
# e passada para variável por meio de um input.
porta = "f"
janela = "f"

alarme = (porta == 'a') or (janela  == 'a')
msg = 'Alarme disparado? ' + str(alarme)
print(msg)

print('-'*30)

#----------------------------------------------------------------
# Exemplo 3 NOT

print('Exemplo - 3 NOT')
print('''Use o operador lógico NOT para inverter o estado atual
de uma variável.''')
print('\n')

x = True

#saida
print("primeiro estado: ", x)

#processamento
x = not x

#saida
print("segundo estado: ", x)

print('-'*30)

#----------------------------------------------------------------



