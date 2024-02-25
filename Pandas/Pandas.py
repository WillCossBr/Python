# O pandas é uma biblioteca de código aberto para
# análise de dados em Python. Entre suas vantagens
# estão a capacidade de lidar com dados de tipos
# diferentes, filtragem, separação, agrupamento,
# ordenação de dados e compativel com outros módulos.

# A principal estrutura de dados Pandas para o uso
# em aprendizagem de máquina e que abordaremos aqui é
# o DataFrame.

# DATAFRAME:
# Representa uma estrutura semelhante à um array de
# duas dimensões, com as suas colunas contendo dados
# de tipos heterogênios, sendo muitas vezes comparado
# com planilhas eletrônicas. Ele possui índices
# distintos para colunas e para linhas, como também
# pode ser criado de formas distintas.

#exemplo:

#importe a bliblioteca
import pandas as pd

#passe os dados
dados_clientes = {"idade":[22,52,31],
                  "nacionalidade":["br", "ita", "esp"],
                  "altura": [1.70,1.75,1.82],
                  "peso": [75,80,65],
                  "sexo": ["fem", "masc", "fem"],
                  "gosta de futebol": [True,True, True],
                  "salário": [2500,2000,4500]}

#cria a tabela com pandas
df_clientes = pd.DataFrame(data=dados_clientes,
index=["Ana","Beto","Bia"])

#imprime toda a tabela
print(30*'-')
print(df_clientes)
print(30*'-')

#imprime somente coluna: idade
print("Apenas a coluna da idade:")
print(df_clientes["idade"])
print(30*'-')
