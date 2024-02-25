#vetorização: A vetorização em Python refere-se ao
#processo de otimizar código para operar em arrays
#ou listas de dados de uma maneira mais eficiente,
#aproveitando operações vetorizadas oferecidas por
#bibliotecas especializadas, como NumPy.
#Em vez de iterar explicitamente sobre elementos
#em um loop, a vetorização permite que você execute
#operações em conjuntos de dados inteiros de uma vez.

#exemplo sem vetorização:

#variaveis
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
resultado = []

#loop -> i iterar o tamanho total de lista1 = 5
for i in range(len(lista1)):

    #atribua ao resultado a soma de lista1 + lista2
    resultado.append(lista1[i] + lista2[i])

#mostra o resultado após somado as duas listas
print('-'*30)
print("Soma de listas, sem vetorização:")
print(resultado)
print('-'*30)

#exemplo com vetorização:

#importe o módulo
import numpy as np

#variaveis
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])
resultado = []

resultado = array1 + array2

print("Soma de listas com vetorização: ")
print(resultado)
print('-'*30)

#exemplo3

#idade e salário
cliente_01 = [35, 2500]

todos_clientes = [[37, 2500],
                  [25, 4500],
                  [42, 6500],
                  [41, 1500],
                  [33, 3500],
                  [45, 1200],
                  [43, 2245],
                  [36, 25000],
                  [18, 8000]]

#atribui a lista(todos_clientes) ao array(todos)
array_todos = np.array(todos_clientes)

#cria uma matriz com cliente_01 com a mesma quantidade
#de linhas de array(todos) para poder compara-la:

array_cli_01 = np.array([cliente_01 for _ in range(array_todos.shape[0])])
comparacao = array_todos-array_cli_01

#imprimindo resultados:
print("lista de idade, salário: ")
print("Um cliente")
print(cliente_01)

print('\n')

print("todos os clientes: ")
print(array_todos)

print('\n')
print("Comparação da diferença de um cliente para os outros clientes:")
print(comparacao)

print('-'*30)





