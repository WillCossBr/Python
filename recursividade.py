#----------------------------------------------------------------
#recursividade

#Fórmula geral para o fatorial:

#caso-base
#fatorial(num) = 1, se num = 0 ou se num = 1

#caso recursivo
#fatorial(num) = num * fatorial(num-1), para num > 1

#ex
# 4! -> * fatorial(3) = 4 * 3 fatorial(2) = 4 * 3 * 2 * fatorial(1) ->
#4! -> 4 * 3 * 2 * 1 = 24

print('-'*30)

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    x = int(input("Digite um número inteiro positivo para calcular seu fatorial: "))
    try:
        res = fatorial(x)
    except RecursionError:
        print(f"O número fornecido é muito grande ou negativo.")
    else:
        print(f'O fatorial de x é: {res}')

print('-'*30)

#----------------------------------------------------------------