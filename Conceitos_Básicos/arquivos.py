#----------------------------------------------------------------
# Manipulação de arquivos de texto.

# manipulador = open('arquivo.txt', 'r', encoding='utf-8')
# print(f'\Método read():\n')
# print(manipulador.read())

# print(30*'-')

# print(f'\Método readline():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(30*'-')

# print(f'\Método readlines():\n')
# print(manipulador.readlines())

#----------------------------------------------------------------
# busca por palavra específica:
# texto = input('Qual o termo desejada procurar no arquivo? ')

# #tratemento de erro:
# try:
#     #atribui o endereço do arquivo a variavel manipulador
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     #abre o arquivo iterando linha por linnha
#     for linha in manipulador:
#         #tira a quebra de linha
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'A string foi encontrada!')
#             print(linha)
#         else:
#             print('String não encontrada!')
#         #imprime
#         print(linha)
# #trata excessão
# except IOError:
#     print(f"Não foi possível abrir o arquivo.")
# #fecha o arquivo
# else:
#     manipulador.close()

#----------------------------------------------------------------
# escrever no arquivo:
# texto = '\nPython é usado em ciência de dados extensivamente'
# try:
#    manipulador = open('arquivo.txt', 'a')
#    manipulador.write(texto)
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

#----------------------------------------------------------------
# gravar listas em arquivos:

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola\n']

# Criar e gravar o arquivo
try:
    manipulador = open('frutas.txt', 'w')
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

# Ler o arquivo criado:
try:
    manipulador = open('frutas.txt', 'r')
    print(manipulador.read())
except IOError:
    print('Não foi possível abrir o arquivo.')
else:
    manipulador.close()

#----------------------------------------------------------------
