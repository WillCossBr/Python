#----------------------------------------------------------------
#Funções:
#Modularização, Reúso de Código, Legibilidade

#sintaxe:

#def <nome_função> ([argumentos]):
#    <instruções>

#----------------------------------------------------------------
#Função de imprimir mensagem:

print(30*'-')

print('Função imprimir mensagem:')
print('\n')
def mensagem():
    print("Bóson Treinamentos em Tecnologia")
    print('Curso Completo de Python.')

mensagem()
print(30*'-')

#----------------------------------------------------------------
#Função com argumentos:

print('Função com argumentos: ')
print('\n')
def soma(a, b):
    print(f'soma de {a} + {b}')

soma(12, 7)
print('-'*30)

#----------------------------------------------------------------
#Função usando return:

def mult(x, y):
    return x * y
#return = encerra a função e retorna o valor de x * y

a = 5
b = 8
c = mult(a, b)  #return =retorna o resultado da função para c

print('função usando return:')
print(f'O produto de {a} * {b} é: {c}')
print('-'*30)

#----------------------------------------------------------------
#função de divisão por zero (Impossiveis):
#
#print('Função com tratamento de erro, caso divida por zero!')
#def div(k, j): #o denominador não pode ser zero!
#    if j != 0:
#        return k / j
#    else:
#        return 'Impossível dividir por zero!'
#
#if __name__ == '__main__':
#    a = int(input('Digite outro número: '))
#    b = int(input('Digite outro npumero: '))
#
#    r = div(a, b)
#    print(f'{a} dividido por {b} = {r}')
#    print('-'*30)
#
#----------------------------------------------------------------

def quadrados(val):                 #função vai receber valores
    quadrados = []                  #lista vazia
    for x in val:                   #itera a lista
        quadrados.append(x ** 2)    #adiciona os valores dentro da lista
    return quadrados


if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultado = quadrados(valores)
    for g in resultado:
        print(g)

#----------------------------------------------------------------