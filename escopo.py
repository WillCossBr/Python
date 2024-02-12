#----------------------------------------------------------------
#escopo

#global = todo o código
#local = somente na função

var_global = 'Curso Completo de Python'

def escreve_texto():

    # muda o conteúdo dentro da var_global
    # sem esse comando a função acaba criando outra
    # variável com o mesmo nome.
    global var_global
    var_global = "Banco de Dados com SQL"
    var_local = 'Fábio dos Reis'
    print(f"Variável Global: {var_global}")
    print(f'Vaviável local: {var_local}')

if __name__ == '__main__':
    print('-'*30)
    print(f'Executar a função escreve_texto()')
    escreve_texto()

print('-'*30)
print("tenta acessar as variáveis diretamente")
print(f"Variável Global: {var_global}")
print('-'*30)

#----------------------------------------------------------------