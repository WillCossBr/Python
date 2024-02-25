#O termo "broadcasting" em Python refere-se a uma 
# funcionalidade que permite a realização de operações
# entre arrays de diferentes formas e tamanhos sem a 
# necessidade de explicitamente transformar esses arrays
# para tamanhos compatíveis.
# O NumPy, uma biblioteca popular para computação 
# numérica em Python, é conhecido por utilizar 
# broadcasting para facilitar operações em arrays.

#A ideia principal por trás do broadcasting é estender 
# automaticamente as dimensões dos arrays menores para 
# que possam ser compatíveis com os arrays maiores. 
# Isso ocorre durante a execução da operação, sem a 
# necessidade de replicar dados ou expandir manualmente
# as dimensões.

#Diferença vetorização e broadcasting:
# Vetorização: é que vetorização faz operações
# otimizadas entre vetores de dimensoes iguais.

# Broadcasting: faz operações entre vetores de
# dimensões variadas, ajustando ambos vetores para
# o mesmo tamanho.

#exemplo:

print("Uso de broadcasting: ")

#importe o módulo
import numpy as np

#cria duas listas:

#lista bidimensional:
lista_x = np.array([[1,2,3,4,5],[9,8,7,6,5]])# 10 elementos

#lista unidimensional:
lista_y = np.array([10,20,30,40,50])# 5 elementos

#Soma de listas com dimensão diferentes:
resultado = lista_x + lista_y

#imprime na tela:
print('-'*30)
print('Soma das listas: ')
print(resultado)
print('-'*30)