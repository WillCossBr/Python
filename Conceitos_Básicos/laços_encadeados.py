#laços encadeados
#um laço for dentro de outro

for cont_ex in range(1,6):
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5, 0, -1):
        print('Valor:', cont_in)

print("Fim dos laços")
print('-'*30)

#----------------------------------------------------------------
#Exemplo - 2
#gerador de números randômicos(Aleatórios)

import random

for A in range(1,6):
    print(f'\Conjunto {A}')
    for B in range(5):
        num = random.randint(1,100) #randint = randômicos inteiros
        print(f'Valor: {num}')

print('-'*30)

#----------------------------------------------------------------
