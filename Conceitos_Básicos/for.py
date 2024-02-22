#----------------------------------------------------------------
#laço de repetição for:
#itera sobre os item de uma lista

lista = [2,6,9,4,0,12,3,7]

for item in lista:
    print(item)
    
print('-'*30)

#----------------------------------------------------------------
#iterar sobre letras de uma palavra

palavra = 'python'

for letra in palavra:
    print(letra)

print('-'*30)

#----------------------------------------------------------------
#iterar com função range (sem a geração de uma lista prévia)
#range(x) = x é a quantidade de vezes que deseja iterar a função.

for numero in range(1,11):
    print(numero)

print('-'*30)

#----------------------------------------------------------------
#itera o nome que o usuário digitar em 10 vezes

print('Itera o nome digitado 10 vezes')
print('\n')
nome = input('digite seu nome: ')

#laço
for x in range(10):
    print(f'{x+1} {nome}')

print('-'*30)

#obs: função range pode usar três parametros
#range(valor_inicial, valor-final, incremento)
#exemplo:
# for i in range (0, 100, 5)
# 0 = começa em zero
# 105 = finaliza o laço (em 100)
# 5 = itera o laço de 5 em 5 saltos... 0, 5, 10, 15, 20 etc...

for i in range(0,105, 5):
    print(f'',i,',', end='')

print('\n')
print('-'*30)

#----------------------------------------------------------------
#exercício usando for

print("""Faça a seguinte tupla:
 pedras = ("Rubi", "Esmeralda", "Quartzo", "Safira", "Diamante", "Turmalina")
itere a tupla usando o laço for, porém sem aparecer a pedra de Quartzo!""")
print('\n')

#variaveis
pedras = ("Rubi", "Esmeralda", "Quartzo", "Safira", "Diamante", "Turmalina")

for pedra in pedras:
    if pedra == 'Quartzo':
        continue #encerra uma iteração atual do laço, e continua o laço.
    print(pedra)

print('-'*30)

#----------------------------------------------------------------
