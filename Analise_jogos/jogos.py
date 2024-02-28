#dados do jogo double da blaze
#Preparar os dados corretamente para usa-los:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

local = "/home/william/Python/Analise_jogos/dados.csv"

arquivo = pd.read_csv(local)

#dados estão com tipos diferentes
print(60*'-')
print('Os tipos de dados são: ')
print(arquivo.dtypes)
print(60*'-')

#1 - tratar os valores faltantes(NaN) com zeros:
arquivo = arquivo.fillna(0)

#salva o arquivo modificiado com zeros:
arquivo.to_csv(local, index=False)

#2 - converter todos os dados para tipo int:
arquivo['vermelhos'] = arquivo['vermelhos'].astype(int)
arquivo['pretos'] = arquivo['pretos'].astype(int)
arquivo['brancos'] = arquivo['brancos'].astype(int)

#dados ja convertidos para int:
print("Dados ja convertidos para int: ")
print('Os tipos de dados são: ')
print(arquivo.dtypes)
print(60*'-')

#mostrar dados:
print(arquivo)
print(60*"-")

#-----------------------------------------------------------------#
#Apresentar os dados em forma de gráficos:

#cores de cada barra
cores = ['red', 'black', 'white']

#cria o gráfico
ax = arquivo.plot(kind='bar', color=cores)

#adiciona rotulos aos eixos e títulos ao gráfico
plt.title('Gráfico de Barras')
plt.xlabel('ìndices')
plt.ylabel('Valores')

#cor de fundo:
ax.set_facecolor('lightgrey')

#exibe o gráfico
plt.show()

#-----------------------------------------------------------------#