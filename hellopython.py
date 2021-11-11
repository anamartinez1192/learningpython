print('hello')
#Case sensitive (Case matters!)
#fruit and Fruit are different variables
#must start with a letter
#can contain numbers
#underscores allowed in variable names
# not allowed + "/" -

#using quotes within strings
#double = "She said, \"That's a great tasting apple!\""
#single = 'She said, "That\'s a great tasting apple!"'

#the len() functions
fruit = 'apple'
fruit_len = len(fruit)
print(fruit_len)

#Nesting functions
print(len('apple'))
###BASIC OOP
#methods are functions run against an object
#everything in python is an object
#every object has a type
#the lower() string method
fruit = 'APPLE'
print(fruit.lower())
Fruit = 'apple'
print(Fruit.upper())

#repeating strings
print('-'*10)

happiness = 'happy ' *3
print(happiness)

#the sr() function
version = 3
print('I love python '+str(version) +'.')

#formatting strings

print('I {} Python.'.format('love'))
print('{} {} {}'.format('I', 'love', 'Python.'))

print('I {0} {1}, {1} {0}s me.'.format('love', 'Python'))

first = 'I'
second = 'love'
third = 'Python'
print('{} {} {}.'.format(first,second,third))

version = 3
print('I love python {}.'.format(version))

#formatting strings: esto puede ayudar a generar tablas
#el 0 y el 1 que se muestran en el ejemplo son la posiciones de los objetos
#y el 8 es el número máximo de caracteres
print ('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print ('{0:8} | {1:8}'.format('Apple', 3))
print ('{0:8} | {1:8}'.format('Oranges', 10))

#formatting strings alignment
# <left
# > right
#^ Center

#formatting strings - Data types
# f Float
# .Nf N = the number of decimal places
#example:
# {:.2f}

#formatting strings
print('{0:8} | {1:<8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:<8.2f}'.format('Apple', 2.33333))
print('{0:8} | {1:<8.3f}'.format('Oranges', 10))

#getting user input
#input() accepts standard input
#input('prompt to display')

fruit = input('Enter a name of a fruit: ')
print('{} is a lovely fruit.'.format(fruit))
