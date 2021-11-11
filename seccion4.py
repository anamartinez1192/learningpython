"""Functions
Reglas no escritas :3
dry = dont repeat yourself
write one time, use many times"""

"""Para crear una función, se hace lo siguiente:
def <function_name>():
    #code block"""

#definir una función
def say_hi():
    print('Hi!')

#llamar a una función
say_hi()

"""la función debe ser definida antes de ser llamada"""

#funciones con parámetros
#parámetros son como variables que pueden ser usados
#dentro de la función.

def say_hi(name):
    print('Hi {}!'.format(name))

say_hi('Jason')
say_hi('everybody')

"""una vez definido el parámetro, la función espera el valor
de dicho parámetro"""

#para hacer opcional el parámetro, dale un valor
#por default al parámetro de la siguiente manera

def say_hi(name='there'):
    print('Hi {}!'.format(name))

say_hi()
say_hi('Jason')

"""las funciones aceptan múltiples parámetros, se separan
por medio de comas"""

def say_hi(first, last):
    print('hi {} {}!'.format(first, last))

say_hi('Alex', 'Pilow')

#el orden de los parámetros definidos en la función es importante

def say_hi(first, last):
    print('hi {} {}!'.format(first,last))

say_hi(first ='Nana', last='Chan')
say_hi(last = 'nana', first = 'chan')

#parámetros opciones y obligatorios pueden combinarse en una misma función

def say_hi(first, last='martínez'):
    print('hi {} {}!'.format(first, last))

say_hi('chan')
say_hi('nana', 'chan')

#funciones, part 2
"""al documentar las funciones, estamos escribiendo
qué hace esa función o porqué existe. Para poder traer esta 
información, hacemos uso de la función help de la siguiente manera"""

def say_hi(first, last='gonzalez'):
    """say hello motherfucker"""
    print('hi {} {}'.format(first, last))

help(say_hi)

#las funciones no solo hacen una tarea, también
#pueden regresar datos usando el stament return

def odd_or_even(number):
    """determina si un número es par o impar"""
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

odd_or_even_string = odd_or_even(7)
print(odd_or_even_string)

def is_odd(number):
    """determina si un número es impar."""
    if number % 2 == 0:
        return False
    else:
        return True

print(is_odd(7))
#no es necesario asignar el valor de la variable de la función
#a otra variable (como en el 
# ejemplo antes de este), se puede imprimir directamente como
#en el ejemplo recién mostrado.

#se pueden crear funciones que llamen a otras funciones

def get_name():
    name = input('cual es tu nombre?')
    return name
def say_name(name):
    print('Tu nombre es {}'.format(name))

def get_and_say_name():
    """obtiene y muestra el nombre"""
    name = get_name()
    say_name(name)

get_and_say_name()

