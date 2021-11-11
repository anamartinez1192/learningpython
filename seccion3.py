#Booleans
# true or false

#comparators
""" == equal to
> greater than
>= greater than or equal
< less than
<= less than or equal
!= not equal"""

"""TRUTH TABLE
true and true is true
true and false is false
false and true is false
false and false is false

true or true is true
true or false is true
false or true is true
false or false is false

not true is false
not false is true"""

"""ORDER OF OPERATIONS FOR BOOLEANS
not
and
or"""

"""Controlling the order of operations
Anything surrounded by parenthesis is
evaluated first and as its own unit"""

#these are the same:
#true and false or not false
#(true and false) or (not false)
#((true and false) or (not false))

#Conditionals

if 37 < 40:
    print("treinta y siete es menos que cuarenta.")

#Code blocks
"""Block one
    block two
    block two
        block three
block one
block one"""

age = 31
if age >= 35:
    print('Eres lo suficientemente viejo para ser presidente.')

print('Ten un buen día!')

age = 31
if age >=35:
    print('Eres lo suficientemente viejo para ser presidente.')
else:
    print('No eres lo suficientemente viejo para ser presidente :(')

print('Anyway, ten un buen día!')

age = 29
if age >= 35:
    print('jeje')
elif age >= 30:
    print('jajaja')
else:
    print('estás muy chavo aún')

print('go away!')

age = 99
if age >= 35:
    print('ya estás muy viejo')
elif age >= 30:
    print('estás viejo pero no tanto')
elif age >= 25:
    print('estás en buena edad')
else:
    print('nombre, muy chavo mijo')

print('go away, again!')

