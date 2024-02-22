import csv

#dados a serem inseridos:
registro_novo = ["6:00","12:00","14:30","20:00"]

#caminho do arquivo a ser escrito
diretório = '/home/william/Python/Manipula_Arqs/despertador.csv'

#modo 'a' (append) adiciona dados no final do arquivo
with open(diretório, 'a', newline='') as desp:
    escrever = csv.writer(desp)

    #escrever o registro novo no arquivo
    escrever.writerow(registro_novo)

#msg de confirmação
print('Registro adicionado com sucesso!')

#visualizar o arquivo csv
print(30*'-')
with open(diretório, 'r', encoding='utf-8') as desp:
    ler = csv.reader(desp)

    for linha in desp:
        print(linha)

print('-'*30)

