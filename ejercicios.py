"""escriba un algoritmo que lea del 
teclado un número entero y que compruebe si el número
es menor que 10. Si no lo está, debe volver a leer el número
repitiendo la operación hasta que el usuario escriba
un valor correcto. Finalmente, debe escribir por pantalla
el valor leído cuando este sea correcto"""

numero = int(input("ingrese un número: "))
while numero >= 10:
    numero = int(input('ingrese un número nuevamente: '))

if numero < 10:
    print("número correcto: " +str(numero))

"""modifique el algoritmo del problema anterior
para que en vez de comprobar que el número sea menor
que 10, compruebe que se encuentra en rango 0 - 20"""
numero = int(input("ingrese un número, pues: "))
while numero > 20:
    numero = int(input("ingrese un número nuevamente, plis: "))
if numero >= 0 and numero <= 20:
    print("número correcto: " +str(numero))

"""modifique el algoritmo del problema anterior
para que cuente las veces que ha leído un número 
de teclado y escriba el resultado por pantalla"""
contador = 0
numero = int(input("ingrese un número, again: "))
while numero != 0:
    contador +=1
    numero = int(input("ingrese un número, jeje: "))

print("resultado: " +str(contador))

"""modifique el algoritmo anterior para que se realicen 
5 lecturas por teclado como máximo"""
numero = int(input("otra vez, otro número: "))
contador = 1
while contador <= 5 and numero > 20:
    numero = int(input("ingrese otro número: "))
    if numero >= 0 and numero<=20:
     contador += 1
print("inputs: " +str(contador))
#respuesta correcta
"""contador = 1
numero = int(input("Ingrese un número"))
while numero>20 or numero<0:
     numero = int(input("Ingrese un número"))
     contador += 1
    if contador==5:
        print ("Máximo número de intentos alcanzado")
    break

print ("Número ingresado:" +str(numero))
print ("Número de intentos:"+str(contador))"""

"""Escriba un algoritmo que calcule e imprima la suma de 
los n primeros números enteros positivos. El valor de n debe
leerse del teclado y ser ingresado por el usuario."""
#estudiarlo, no lo hice yo
suma = 0
numero = int(input('ingrese un número, pibe: '))
while numero>0:
    suma = (numero*(numero+1))/2
    break
print("número ingresado: " +str(numero))
print("suma total: " +str(suma))

"""Escriba un algoritmo que sume los números ingresados
por el usuario hasta que el usuario ingrese el número 0
(detenre las preguntas ante este escenario)."""
suma = 0
numero = int(input("escriba un número, pana: "))
while numero > 0:
    suma+=numero
    numero= int(input("escriba otro número, amigo: "))

print("la suma total es: "+str(suma))

"""Escriba un algoritmo que sume los números ingresados
por el usuario y cuando la suma sea superior a 100 deje
de pedir números y muestre el total"""
suma = 0
numero = int(input("vamos, ponga el número: "))
while suma < 100:
    numero = int(input("vamos, ponga el número: "))
    suma+=numero
    numero = int(input("vamos, otro número: "))
print("suma total: "+str(suma))

#forma correcta
suma = 0
numero = int(input("vamos, ponga el número: "))
while numero!=0:
    suma+=numero
    if suma>100:
        break
    numero = int(input("vamos, ponga el número: "))
    
print("la suma es: " +str(suma))

