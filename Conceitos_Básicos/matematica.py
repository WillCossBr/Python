#----------------------------------------------------------------
#Funções builtin

valores = [2,5,8,-1,0,11,7,-6]
print(max(valores))
print(min(valores))
a = -5
b = 4
print(abs(a)) #valor absoluto
print(pow(a, b)) #exponenciação
c = 2.789011
print(round(c,3)) #arredondamento

#----------------------------------------------------------------
#módulo math

import math

x = 8
y = 100

raiz_quadrada = math.sqrt(x)
print(f'raiz quadrada de 8 é: {raiz_quadrada}')
print(f'raiz arredondada pra cima: {math.ceil(raiz_quadrada)}')
print(f'raiz arredondada pra baixo: {math.floor(raiz_quadrada)}')

#----------------------------------------------------------------
#Logaritmo
logaritmo = math.log10(y)
print(logaritmo)

#----------------------------------------------------------------
#constante de pi:
print(math.pi)

#----------------------------------------------------------------
#fatorial
print(math.factorial(x))

#----------------------------------------------------------------
#divisão pelo infinito:
print(x / math.inf)

#----------------------------------------------------------------
