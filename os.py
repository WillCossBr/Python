#----------------------------------------------------------------
# Comandos Python OS:

# import os
# importa o módulo os

# os.listdir()
# lista as pastas do diretório atual

# os.chdir('caminho do local')
# move para o diretório desejado

# os.mkdir('nome da pasta')
# cria uma pasta

# os.getcwd()
# lista o caminho do diretório atual

# os.rename('caminho + nome antigo', 'caminho + nome novo')
# troca o nome de uma pasta

# os.rmdir('nome da pasta')
# remove uma pasta (diretórios vázios)

# os.path.basename(os.getcwd())
# nome do diretório atual

# os.path.dirname(os.getcwd())
# mostra o caminho que o diretório está dentro

# criação de pastas recursivas(uma dentro da outra)
# pasta_pai = os.getcwd()
# novas_pastas = 'América/Brasil/Ilhabela'
# caminho = os.path.join(pasta_pai, novas_pastas)
# print(caminho)
# os.makedirs(caminho)

# os.path.exists('caminho')
# verifica se um caminho de diretório existe (True ou False)

# os.path.isdir('caminho')
# pergunta se o local é um diretório

# os.path.isfile.('caminho')
# pergunta se o local é um arquivo

# manipulador = open('nome do arquivo.txt(arq.txt)', 'parametro(x)')
# cria um arquivo

# manipulador.close()
# fecha o manipulador

# os.path.splitext('nome da variável')
# divide o nome do arquivo do seu tipo

# os.remove('caminho')
# remove um arquivo

# bibliotecas arternativas ao os:

# import pathlib
# importa a biblioteca pathlib

# import shutil
# importa o módulo shutil

# shutil.rmtree('caminho')
# remove a árvore de arquivo (pastas + arquivos)

#----------------------------------------------------------------

import os

print(30*'-')
print("Script que muda o nome dos arquivos: ")

os.chdir('/home/william/python/teste')
print(f'Diretório atual: {os.getcwd()}')

padrão_nome = input("""Qual o padrão de nomes de
nomes de arquivos a usar (sem a extensão)?""")

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrão_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print("Arquivos renomeados.")

#----------------------------------------------------------------