#----------------------------------------------------------------
#usando função map para iterar a lista e
#lambda para extrair os quadrados dos itens da lista

print('-'*30)
print("Função map() + lambda() para extrair quadrados: ")
numeros = [1,4,7,10,12,21]

quadrados = list(map(lambda num: num**2, numeros))
print(quadrados)
print('-'*30)

#----------------------------------------------------------------
#simplificando a sintaxe: compreensão de lista

print("iteração de lista simplificada: ")
quadrados1 = [num**2 for num in numeros]
print(quadrados)

print('-'*30)

#----------------------------------------------------------------
#criar uma lista de números pares de 0 a 10

print("""Criar uma lista de números pares de 0 a 10:
usando crompreensão de lista: """)

pares = [i for i in range(11) if i % 2 == 0]
print(pares)

print('-'*30)

#----------------------------------------------------------------
#programa conta a quantidade de vogais
#dentro de um texto

print("""Programa que conta a quantidade de vogais
dentro de um texto: """)

frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

lista_vogais = [j for j in frase if j in vogais]
print(f'A frase possui {len(lista_vogais)} vogais:')
print(lista_vogais)

print(30*'-')
#----------------------------------------------------------------
#usar 2 laços for para realizar a multiplicação
#dos números de uma lista pela outra

#distributiva entre valores de duas listas

print("""Usar dois laços for para realizar a
multiplicação dos números de uma lista pela outra: """)

distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)

print('-'*30)

#----------------------------------------------------------------