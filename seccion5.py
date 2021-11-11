"""Listas
una lista es un tipo de dato que contiene
una ordenada colección de objetos
Los objetos pueden ser de varios tipos de datos
incluso puedes tener listas de listas"""

"""creando listas

list_name = [item1, item2, itemN]
list_name = []
list_name[index]"""

#ejemplo

animals = ['man', 'bear', 'pig']
print(animals[1])
print(animals[0])
print(animals[2])

#no solo se puede acceder a los valores 
#por index, también se pueden establecer por index

animals = ['man', 'bear', 'pig']
print(animals[0])
animals[0] = 'cat'
print(animals[0])

#se puede acceder a los últimos objetos de la lista 
#usando el signo de negativo -

animals = ['man', 'bear', 'pig']
print(animals[-1])
print(animals[-2])
print(animals[-3])

#para agregar un objeto al final de la lista, usa el método
#append y agrega el item a poner en la lista

animals = ['man', 'bear', 'pig']
animals.append('cow')
print(animals[-1])

#para agregar múltiples items al final de la lista
#usa el método extend

animals = ['man', 'bear', 'pig']
animals.extend(['cow', 'duck'])
print(animals)

#aquí se agregaron más items a la lista por medio de otra lista
more_animals = ['horse', 'dog']
animals.extend(more_animals)
print(animals)

#se pueden agregar items en cierta ubicación de
#la lista utilizando el método insert

animals = ['man', 'bear', 'pig']
animals.insert(0,'horse')
print(animals)
animals.insert(2,'duck')
print(animals)

#Slices
# list[index1:index2]
# list[:index2]
# list[index1:]

animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

some_animals = animals[1:4]
print('some animals:   {}'.format(some_animals))

first_two = animals[0:2]
print('First two animals: {}'.format(first_two))

first_two_again = animals[:2]
print('First two animals again: {}'.format(first_two_again))

last_two = animals[4:6]
"""aquí me envía duck and horse"""
print('last two animals: {}'.format(last_two))

last_two_again = animals[-2:]
"""aquí me envía duck and horse"""
print('last two animals {}'.format(last_two_again))

#string slices
#string son un conjunto de caracteres(como una lista), así se extrae una parte de ese string
part_of_a_horse = 'horse'[1:3]
print(part_of_a_horse)

#Exception Handling
#Finding an item in a list
animals = ['man', 'bear', 'pig']
bear_index = animals.index('bear')
print(bear_index)

#exception handling

animals = ['man', 'bear', 'pig']
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No cats found.'
print(cat_index)

#loops
#looping through a list
""" for item_variable in list_name:
    #code block

item_variable = list[0]
item_variable = list[1]
item_variable = list[N]

"""
animals = ['man', 'bear', 'pig']

for animal in animals:
    print(animal.upper())

#while loop
""" while condition:
        #code block
"""
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

index = 0
while index < len(animals):
    print(animals[index])
    index += 1