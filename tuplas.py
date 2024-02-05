#tuplas
# São imutáveis

#criação
tupla = (2,4,6,7,9)
print(tupla)

#----------------------------------------------------------------
#elemento específico:

halogenios = ("F","Cl","Br","I","At")
print(halogenios[3])

#----------------------------------------------------------------
#concatenação:

gases_nobres = ('He','Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
print(elementos)

#----------------------------------------------------------------
#varrer a tupla:
# checar quantas vezes aparece o número 5 na tupla

t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(t1.count(5))

#----------------------------------------------------------------
#trechos da tupla:

print(t1[2:5])

#----------------------------------------------------------------
#Operações não disponíveis em tuplas:

#.sort(), append(), reverse(), pop()...

#----------------------------------------------------------------
#iteração com tupals:

for elemento in elementos:
    print(f'Elementos químicos: {elemento}')

#----------------------------------------------------------------
#passar uma tupla para dentro de uma lista:
    
grupo17 = list(halogenios)
print(grupo17)

#----------------------------------------------------------------
#passar uma lista para dentro de uma tupla:

grupo1 = ['li', 'na', 'k', 'rb', 'cs', 'fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

#----------------------------------------------------------------
