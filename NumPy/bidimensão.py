#criando uma matriz bidimensional

#importe a biblioteca NumPy
import numpy as np

#criando a matriz
matriz = np.array([[1,2,3],[4,5,6]])

#obtendo a forma da matriz
forma = np.shape(matriz)

#imprimindo a forma
print(30*'-')
print("Forma da matriz", forma)
print("Duas linhas e três colunas.")
print(30*'-')

#imprimindo a matriz
print("IMPRIMINDO A MATRIZ: ")

#modo simples
print('modo simples: ')
print(matriz)

#modo identado e com indices
print('modo identado e com indices: ')
print(matriz[0])
print(matriz[1])
print(30*'-')

#imprimindo item específico, buscando por indice
#obs: os indices começam a ser contados por zero.
print("imprimindo item espefíco: ")
print('matriz[1][2]: linha[1], coluna[2]')
print(f'Conteudo = {matriz[1][2]}')
print(30*'-')

#Operação do soma na matriz bidimensional:

#axis=0 -> soma das colunas
soma_colunas = np.sum(matriz, axis = 0)

#axis=1 -> soma das linhas
soma_linhas = np.sum(matriz, axis = 1)

print('                         Soma das linhas')
print('                ',matriz[0], soma_linhas[0])
print('               +',matriz[1], soma_linhas[1])
print('Soma das colunas',soma_colunas)
print(30*'-')
