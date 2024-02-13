#----------------------------------------------------------------
# exceção é um objeto que representa um erro
# que ocorreu ao executar o programa.

#blocos try(tentar)... except(exceção)

#----------------------------------------------------------------
# tratar divisão por zero:

print('-'*30)
print("Exemplo - 1, Tratamento de erro (exceção)")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

#round para arredondar

#tratar
try:
    r = round(n1 / n2, 2)
#exceção de divisão por zero.
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
#caso não apareça o zero o código continua
else:
    print(f'Resultado: {r}')

print('-'*30)

#----------------------------------------------------------------
#exemplo - 2

print('Exemplo - 2, exceção com função')

#função de divisão:
def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':

    #caso ocorrá uma exceção o laço mantém o programa rodando
    while True:
        #tratar
        try:
            x1 = int(input('Digite um número: '))
            x2 = int(input('Digite outro número: '))
            break
        #exeção de entrada errada. Só aceita números inteiros.
        except ValueError:
            print("Ocorreu um erro ao ler o valor. Tente novamente.")


    #tratar
    try:
        #atribui o retorno da função a variável result
        result = div(x1 ,x2)
    #exceção de divisão por zero
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    #excessão desconhecida qualquer
    except:
        print("Ocorreu um erro desconhecido...")
    #caso ocorra tudo bem, o programa continua e exibe o resultado
    else:
        print(f"Resultado: {result}")
    #bloco finally sempre será executado.
    finally:
        print("Fim do cálculo")

    print('-'*30)

#---------------------------------------------------------------- 