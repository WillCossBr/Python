#Manipalação de arquivos CSV

# Comma-Separated Values ou CSV são arquivos  de texto separados por vírgula.
# É uma forma de organizar dados e geralmente os arquivos de texto csv são
# convertidos em tabelas.

import csv

print(30*'-')
print("Abrindo arquivos CSV: ")

with open('/home/william/Python/Manipula_Arqs/CSV/funcionários.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq)

    for linha in leitor:
        print(str('    '.join(linha)))

print(30*'-')
