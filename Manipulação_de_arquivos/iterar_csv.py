import csv

print(30*'-')
print("Iterando arquivos CSV: ")

with open('/home/william/Python/Manipula_Arqs/produtos.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq)

    ultimo_registro = 5

    for i, registros in enumerate(leitor):

        if i < ultimo_registro:
            print(f'indice: {i}, {registros}')

print(30*'-')