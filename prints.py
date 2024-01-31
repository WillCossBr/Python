#Função Print()

#Sintaxe:
#print(objeto, argumento)

#função print
print('-'*30)
print('Função print')
print('\n')

#imprime uma mensagem direta
print("1° - Impressão direta")
print('print(aula de python)')
print('\n')
print('-'*30)

#----------------------------------------------------------------
#imprime o conteúdo de uma variável
print("2° - impressão de variável")
print("mensagem = 'Olá Mundo'")
print('print(mensagem)')
mensagem = 'Olá Mundo'
print(mensagem)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#imprime uma mensagem direta e uma variavel
print("3 - impressão de uma mensagem direta e uma variável")
print('"print(Madição do - ", mensagem)')
print("Maldição do - ", mensagem)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#impressão de duas variaveis
print("3 - impressão de uma duas variáveis")
print("x1 = 'programação'")
print("x2 = 'python'")
print("print(x1, x2)")
x1 = 'programação'
x2 = 'python'
print(x1,x2)
print('\n')
print('-'*30)

#----------------------------------------------------------------
#impressão de concatenação de string

print("""Pessa para usuário digitar seu nome e a idade, 
em seguida concatene a mensagem na tela. """)
print('\n')

#variáveis
nome = ""
idade = ""

#entradas
print("Digite seu nome: ")
nome = input()

print("Digite sua idade: ")
idade = input()

#saidas
print('Seu nome é: ' + nome + '. Sua idade é: ' + idade + 'anos.')

print('-'*30)

#----------------------------------------------------------------
#impressão de mensagem sem e com quebra de linha

#sem quebra
print("linha Única")
print('\n')
print("msg sem mudar de linha")
print("Imprime a mensagem")
print('\n')

#com quebra (end='')
print("msg quebrando a linha")
print("imprime a mensagem e permanece na linha.", end='')
print("Continua na mesma linha")
print('-'*30)

#----------------------------------------------------------------
# mensagens complexas

a = 'matemática'
b = 100

#função .format()
print("mensagem Complexa")
print('\n')
print('Na matéria {0} ele(a) tirou {1} na prova.'.format(a,b))
print('-'*30)

#----------------------------------------------------------------
#mensagem f-string

nome = 'William'
idade = 25
msg = f'Meu nome é {nome} e minha idade é {idade} anos.'

print("mensagem f-string")
print('\n')
print(msg)
print('\n')

#calculos com f-string
num1 = 10
num2 = 5

print("calculo com f-string")
print(f'{num1} + {num2} = {num1+num2}')
print('\n')

#formatação de float com f-string
print('formatação de float com f-string')
valor_pi = 3.14159265358979323846
print(f'O valor de PI é: {valor_pi:.2f}')
print('\n')

#caracteres especias com, f-string
print("caracteres especiais (\'$%etc...)")
print(f'nome:{nome} \tidade:{idade}')

print('-'*30)
#----------------------------------------------------------------