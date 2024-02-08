#----------------------------------------------------------------
#set = conjuntos

#Conjuntos: Não mantêm nenhuma ordem específica. Os elementos 
#em um conjunto são únicos e não possuem índices.
#conjuntos sao delimitados por: {}

print(30*'-')
planeta_anao = {"Plutão", "Ceres", "Eris", "Haumea", "Makemake"}
print(f'conjunto de planetas: \n{planeta_anao}')
print('\n')

print(f'tamanho do conjunto: {(len(planeta_anao))} planetas')
print(f'verifique se "Ceres" está nesse conjunto: {("Ceres" in planeta_anao)}')
print(f'verifique se "Lua" está nesse conjunto: {("Lua" in planeta_anao)}')

print('\n')
print(30*'-')

#----------------------------------------------------------------
#Não aceita item duplicados:

print("'Set's não aceitam elementos duplicados - exemplo: ")

lista = ["Lua", "Vênus", "Sirius", "Marte", "Lua"]

print(f'lista de astros: {lista}')

#set = definir ou modificar
conjunto_set = set(lista)

print(f'Conjunto(set) de astros: {conjunto_set}')
print('\n')
print('''Perceba que na lista a lua se repete duas vezes,
ja no conjunto(set)não.''')
print(30*'-')

#----------------------------------------------------------------
#comparação de set:

lista1 = {"a", "b", "c", "d"}
lista2 = {"a", "b", "c", "d", "e"}

print('Comparação de set: \n')
print('São Iguais?')
print(lista1 == lista2)
print('\n')

print('São diferentes?')
print(lista1 != lista2)
print('\n')

#----------------------------------------------------------------
#união de set's:

print("União de set's")
print(lista1 | lista2) #junta os sets
#ou print(lista1.union(lista2)) #junta os sets
print('\n')

#----------------------------------------------------------------
#interseção de set's:

print("Interseção dos set's")
print(lista1 & lista2)
#ou print(lista1.intersection(lista2)) #exibe os elementos repetidos
print('\n')

#----------------------------------------------------------------
#diferença simétrica:

print("Diferença simétrica dos set's")
print(lista1 ^ lista2)
#ou print(lista1.symmetric_difference(lista2))#diferença entre os sets
print('\n')

#----------------------------------------------------------------
#adicionar elementos a um set

print("adicionar elemento aos set's")
lista1.add('z')
lista1.add('w')
print(lista1)
print('\n')

#----------------------------------------------------------------
#remover elementos a um set

print("remover elementos aos set's")
lista1.remove('w')
#ou lista1.discard("w")
print(lista1)
print('\n')

#----------------------------------------------------------------
#remover um elemento aleatório:

print("remover elemento aleatório")
lista1.pop()
print(lista1)
print('\n')

#----------------------------------------------------------------
#limpar um set

print("limpar um set")
lista1.clear()
print(lista1)
print('\n')

#----------------------------------------------------------------