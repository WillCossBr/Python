#XML ou Extensible Markup Language, é uma linguagem de marcação que permite estruturar dados 
#de forma hierárquica.
#É amplamente utilizado para armazenar e trocar informações entre diferentes sistemas.

#A biblioteca etree.elementTree = (Árvore de elementos), permite navegar pela estrutura dos arquivos xml.

print('-'*30)

#importar o módulo:
import xml.etree.ElementTree as ET

#variavel com o local do arquivo xml
local = "/home/william/Python/Manipula_Arqs/arquivos_xml/bebidas.xml"

with open(local, 'r') as bebidas:

    #função parse() controi uma árvore da estrutura xml do arquivo
    arvore = ET.parse(local)

    #obter a raiz da árvore
    raiz = arvore.getroot()

#função recursiva para ler todas as tags e subtegs:
def print_elementos(elemento, indent=""):
    
    #mostra tag de abertura
    print(f'{indent}<{elemento.tag}>')

    for filho in elemento:
        print_elementos(filho, indent + "  ")
    
    #mostra conteúdo e tag de fechamento
    if elemento.text and elemento.text.strip():
        print(f'{indent} {elemento.text}')
    print(f'{indent}</{elemento.tag}>')

#chama a função
print_elementos(raiz)

print('-'*30)

