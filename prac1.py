#EJERCICIO 1 escribe un programa en python que use tres variables.
#las variables en tu programa serán animal, vegetal y mineral
#asigna un valor string a cada una de las variables.
#tu programa deberá mostrar "aquí hay un animal, un vegetal y un mineral"
#enseguida, muestra el valor para animal, vegetal y mineral
#cada valor debe mostrarse en su propia línea
#el programa mostrará 4 líneas en total
print('###EJERCICIO 1###')
animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'
print('Here is an animal, a vegetable and a mineral: \n{} \n{} \n{}'.format(animal,vegetable,mineral))

#EJERCICIO 2 escribe un programa en python que muestre algo
#al usuario para que ingrese and simplemente repite
#lo que el usuario puso
print('###EJERCICIO 2###')
algo = input('Por favor, escriba algo y teclee enter: ')
print('tú escribiste: \n{}'.format(algo))

#EJERCICIO 3 escribe un programa python que muestre un msj al usuario
#para que ingrese y muestre un gato diciendo lo que tecleó
#el usuario. coloca lo dado por el usuario dentro de una burbuja
#de charla. haz la burbuja de charla que se haga grande o chica
#para que quepa el texto dado por el usuario
print('###EJERCICIO 3###')
algo = input('Por favor, dígale algo al gatito: ')
print('        < {} >'.format(algo))
print('          /')
print(' /\_/\   /')
print('( º.º )')
print(' > ^ <')
#otra forma de hacer el ejercicio 3
text = input('dile algo: ')
text_len = len(text)
print('           {}'.format('_'*text_len))
print('         < {}>'.format(text))
print('           {}'.format('_'*text_len))
print('          /')
print(' /\_/\   /')
print('( º.º )')
print(' > ^ <')

