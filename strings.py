nome = 'Curso de Python'
instrutor = "Fábio"
letra = nome[2]
print(letra)
print(len(nome))
print(nome + ' com ' + instrutor)

#----------------------------------------------------------------

frase = 'vamos aprender Python hoje.'
palavras = frase.split() #divide a frase em palavras baseado no seus espaços
print(palavras)
print(palavras[1])# acessar palavra individualmente
for palavra in palavras:
    print(palavra)

for letra in frase:
    print(letra)

#----------------------------------------------------------------
#retirar um pedaço da string:

print(frase[0:5])
print(frase[6:15])

#----------------------------------------------------------------
#encontrar um char especifíco dentro da string:

email = input('Digite seu email: ')
arroba = email.find('@')
print(arroba)# = a posição do arroba é 5
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

#----------------------------------------------------------------
produtos = 'carbonato de sodio e óxido de zinco'
print('sodio' in produtos) #sodio esta em produtos? True
print('magnésio' not in produtos) #magnésio não esta em produtos? True

#----------------------------------------------------------------
#maiusculo e minusculo

objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste.upper()) #string toda maiuscula
print(objeto_celeste.lower()) #string toda minuscula
print(objeto_celeste.capitalize()) #string primeira letra em maiuscula
print(objeto_celeste.title()) #string primeira letra de cada palavra em maiusculo
print('-'*30)

#método replace = substitui palavras da string

#----------------------------------------------------------------
#retirar espaços em branco:

frase = '   õmega 3 é bom para saúde!    '
print(frase)
print(frase.lstrip()) #l = esquerda
print(frase.rstrip()) #r = direita
print(frase.strip()) # elimina esquerda e 

#----------------------------------------------------------------
#alinhamento de texto para exibição

fruta = 'abacate'
print(fruta)
print(fruta.rjust(20)) #justificar a direita
print(fruta.center(20, "-")) #centralizar
print(fruta.ljust(20)) #justificar a esquerda
print('-'*30)

#----------------------------------------------------------------
#prefixos e sufixos:

p = "Bóson Treinamentos"

#inicio
print('inicio')
print(p.startswith('Bó')) # o texto começa com Bó ? True
print(p.startswith('b')) # o texto começa com b ? False
print('-'*30)

#fim
print('fim')
print(p.endswith('tos')) # o texto começa com Bó ? True
print(p.startswith('x')) # o texto começa com Bó ? True
print('-'*30)

#----------------------------------------------------------------
#docstrings:
#documenta trechos específicos do códigos:

"""
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classes no Python, entre outros locais.
    Respeita deslocamento do texto e é multilinhas.
"""

#pode ser colocadas dentro de variáveis:

texto = '''
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classes no Python, entre outros locais.
    Respeita deslocamento do texto e é multilinhas.
    '''

print(texto)

#----------------------------------------------------------------