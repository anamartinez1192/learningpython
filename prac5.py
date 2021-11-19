"""Crea un programa en python que capture y muestre
una "por hacer" lista de una persona. Continuamente
pregunta al usuario por otro elemento hasta que ingresen
un elemento en blanco. Después de que todos los elementos
sean ingresados, muestra la lista al usuario"""

#PRACTICA NO RESUELTA POR MI
to_do_list = []
finished = False

while not finished:
    task = input('Ingrese la tarea: ')
    if len(task) == 0:
        finished = True
    else:
        to_do_list.append(task)
        print('tarea agregada')

print()
print('Tu lista por hacer: ')
print(' - ' * 16)
for task in to_do_list:
    print(task)

""" leer números enteros de teclado, hasta que el usuario
ingrese el 0. Finalmente, mostrar la sumatoria 
de todos los números ingresados"""


"""numero = int(input('ingrese el número: '))
while numero != 0:
    final = int(numero)
    numero = int(input('ingrese el número: '))
    total = final + numero
   
    #numero = numero + 1
    
print('su total es: ' +str(total))"""

suma = 0
numero = int(input('Ingrese el número: '))
while numero != 0:
    suma += numero
    numero = int(input('ingrese el número: '))
    
print ('Suma total: '+str(suma))

"""leer números enteros de teclado, hasta que el usuario ingrese
el 0. Finalmente, mostrar la sumatoria de todos los 
números positivos ingresados"""

suma = 0
numero = int(input('Ingrese un número: '))
while numero != 0:
    if numero>0:
        suma += numero
    numero = int(input('ingrese el número: '))

print('suma total: ' +str(suma))

"""Leer números enteros positivos de teclado, hasta
que el usuario ingrese el 0. Informar cuál
fue el mayor número ingresado"""

mayor = 0
numero = int(input('ingrese un número positivo: '))
while numero != 0:
    if numero > mayor:
        mayor = numero
    numero = int(input('ingrese un número positivo: '))

print('el mayor es: ' +str(mayor))

"""leer los números enteros positivos desde teclado
e imprimir la suma de los dígitos que
lo componen"""
#ESTUDIARLO MÁS
suma = 0
numero =int(input('número: '))
while numero != 0:
    digito = numero%10
    suma+=digito
    numero=numero//10

print("suma:" +str(suma))

"""Solicitar al usuario que ingrese números enteros
positivos y, por cada uno, imprimir la suma de los dígitos que
lo componen. La condición de corte es que se ingrese
el número -1. Al finalizar, mostrar cuántos de los números
ingresados por el usuario fueron pares"""
#me faltó la suma de los que lo componen
suma = 0
par = 0
numero = int(input('ingrese número entero: '))
while numero >= 0:
    digito = numero%10
    suma+=digito
    numero=numero//10
    numero = int(input('ingrese otro número: '))
    
    if (numero%2) == 0:
        par+=1
print("total de pares: " +str(par))

"""Mostrar un menú con tres opciones: 1.- comenzar
programa, 2.- imprimir listado, 3.- finalizar programa.
A continuación, el usuario debe poder seleccionar
una opción (1, 2 o 3). Si elige una opción incorrecta, 
informarle del error. El menú se debe volver a mostrar luego
de ejecutada cada opción, permitiendo volver a elegir.
Si elige las opciones 1 o 2, se imprimirá un texto.
Si elige la opción 3, se interrumpirá la impresión del menú
y el programa finalizará"""

while True:
    respuesta = int(input("Favor de seleccionar una opción: \n1.- Comenzar programa \n2.- Imprimir listado \n3.- Finalizar programa \n"))
    if respuesta == 1:
        print("texto respuesta 1")
    elif respuesta == 2:
        print("texto respuesta 2")
    elif respuesta == 3:
        print("Bye")
        break
    else:
        print('favor de seleccionar 1, 2 o 3')


"""Solicitar al usuario el ingreso de una frase 
y de una letra (que puede o no estar en la frase). 
Recorrer la frase, carácter por carácter, comparando con la
letra buscada. SI el carácter no coincide, indicar que no hay
coincidencias en esa posición (imprimiendo la posición) 
y continuar. Si se encuentra una coincidencia, indicar
en qué posición se encontró y finalizar la ejecución"""
#estudiar
frase=input("frase: ")
letra=input('letra: ')
i=0
while i!=len(frase):
    if letra!=frase[i]:
        print("no se encontró en posiión " +str(i))
        i+=1
        continue 
    print("se encontró en la posición: " +str(i))
    break

"""crear un programa que permita al usuario ingresar
los montos de las compras de un cliente, cortando
el ingreso de datos cuando el usuario ingrese
el monto 0. Si ingresa un monto negativo, no se debe procesar
y se debe pedir que ingrese un nuevo monto. Al finalizar,
informar el total a pagar, teniendo en cuenta que,
si las ventas superan el total de $1000,
se debe aplicar un 10% de descuento"""
#me faltó agregar la excepción de qué 
#pasa cuando se ingresa un monto negativo
suma = 0
monto = int(input("ingrese un monto: "))
while monto > 0:
    suma+=monto
    monto = int(input("ingresa un monto: "))

if suma <1000:
    print("el total es: " +str(suma))
elif suma>=1000:
    total = suma * 0.90
    print("el total con descuento es: " +str(total))

"""Crear un programa que solicite el ingreso de números 
enteros positivos, hasta que el usuario ingrese el 0.
Por cada número, informar cuantos digítos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares
y de dígitos impares leídos en total"""
#estudiarlo, no lo hice yo
numero=int(input("numero: "))
totalPares=0
totalImpares=0
while numero!=0:
   pares=0
   impares=0
   while numero!=0:   
     ultimodigito=numero%10
     if ultimodigito%2==0:
       pares+=1
       totalPares+=1
     else:
       impares+=1
       totalImpares+=1
     numero=numero//10
   print("El número ingresado tiene " +str(pares)+ " digitos pares y " +str(impares)+ " digitos impares")
   numero=int(input("Otro número: "))
print("Total de dígitos pares:" +str(totalPares))
print("Total de dígitos impares:" +str(totalImpares))

"""Crear un programa que permita al usuario ingresar
títulos de libros por teclado, finalizando el ingreso 
al leerse el string “*” (asterisco). 
Cada vez que el usuario ingrese un string de longitud 1 
que contenga sólo una barra (“/”) se considera que termina 
una línea.Por cada línea completa, informar cuántos dígitos 
numéricos (del 0 al 9) aparecieron en total 
(en todos los títulos de libros que componen en esa línea). 
Finalmente, informar cuántas líneas completas se ingresaron."""
#estudiarlo, no lo hice yo
lineas=0
digitos="0123456789"
cantidadDigitos=0
cadena=input("Cadena: ")
while cadena!="*":
    for caracter in cadena:
        if caracter in digitos:
            cantidadDigitos+=1
    if cadena=="/":
        lineas+=1
        print("Aparecen " +str(cantidadDigitos)+ " dígitos en la línea")
        cantidadDigitos=0
    cadena=input("Cadena: ")
print("Se leyeron "+str(lineas)+" líneas completas")

"""Escribir un programa que solicite el ingreso de 
una  cantidad indeterminada de números mayores que 1,
finalizando cuando se reciba un 0. Imprimir
la cantidad de números primos ingresados"""
primos = 0
numero = int(input("ingrese número plis: "))
while numero > 1:
    if (numero%2) != 0:
        primos +=1
    numero = int(input("ingrese otro número plis: "))

print("los números primos son: " +str(primos))

"""solicitar al usuario que ingrese una frase
y luego informar cuál fue la palabra
más larga (en caso de haber más de una, mostrar
la primera) y cuántas palabras había. Precondición: se 
tomará como separador de palabras el carácter " " (espacio),
ya sea uno o más"""
#estudiarlo, no lo hice yo
frase=input("Frase: ").strip()
cantidad=0
len_p_mas_larga=0
while len(frase) != 0:
    cantidad=cantidad+1
    i=frase.find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra más larga:" +p_mas_larga)
print("Cantidad de palabras:" +str(cantidad))