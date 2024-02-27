# Matplotlib é uma bliblioteca usada para apresentação de dados
# em forma de gráficos de diversos tipos. Ela pode ser combinada
# com outras blibliotecas como Pandas e NumPy.

# Características:
# Diversos tipos de gráficos
# Controle total sobre os elementos do gráfico
# Suporte a gráficos interativos
# Integração com Jupyter
# Qualidade de impressão e exportação

#exemplo:
import matplotlib.pyplot as plt

#pyplot
#permite criação de gráficos simples e rápidos;
#personalização de elementos gráficos;
#controle sobre eixos;
#visualização interativa.


#Variáveis:
x = [1,2,3,4,5]
y = [2,4,6,8,10]

#Criar o gráfico de linha
plt.plot(x,y)

#Adicionar rótulos e títulos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de linha Simples")

#Mostrar o gráfico
plt.show()
