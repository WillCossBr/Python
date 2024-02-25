#Matriz tridimensional

#importe o módulo NumPy
import numpy as np

#criando a matriz
matriz = np.array([[[1,2,3],
                    [4,5,6],
                    [7,8,9]],
                    
                   [[10,11,12],
                    [13,14,15],
                    [16,17,18]],
                     
                   [[19,20,21],
                    [22,23,24],
                    [25,26,27]]])

#Exibindo a matriz tridimensional
print('-'*30)
print("Matriz tridimensional: ")
print(matriz)
print('-'*30)

#Exibir conteudo por indice
print("Busca na matriz com uso de indice: ")
print(f'matriz[1][1][1] =',matriz[1][1][1])
print('-'*30)
