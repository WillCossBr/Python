#Laço de repetição while

print('-'*30)
print('Laço de repetição While')
print('\n')

print("Desenvolva um contador de zero a dez usando o laço de repetição while.")

#variável
contador = 0

#laço
while contador <= 10:
    #saida
    print(contador)
    contador += 1
print("Laço encerrado!")
print('-'*30)

#----------------------------------------------------------------

print('Laço de repetição while infinito')
print('\n')

#variável
nome = None

#laço infinito
while True:
    print("Digite seu nome, ou x para parar: ")
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f"Bem-vindo {nome}!")
    print('\n')

print('Até logo!')
print('-'*30)

#----------------------------------------------------------------
