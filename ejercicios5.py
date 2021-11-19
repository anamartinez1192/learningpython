"""Escribir un programa que pida al usuario una palabra
y la muestre por pantalla 10 veces"""
palabra = input("Diga la palabra: ")
print((palabra+'\n') * 10)

word = input("Introduce una palabra: ")
for i in range(10):
    print(word)

"""Escribir un programa que pregunte al usuario su edad
y muestre por pantalla todos los años que ha cumplido
(desde el 1 hasta su edad)."""
edad = int(input("teclee su edad: "))
for i in range(edad):
    print("Has cumplido "+str(i+1)+ " años")

"""Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números impares desde
1 hasta ese número separados por comas"""
n = int(input("Teclee el número: "))
for i in range(1, n+1, 2):
    print(i, end=' , ')

"""Escribir un programa que pida al usuario un número
entero positivo y muestre por pantalla la cuenta atrás
desde ese número hasta 0 separado por comas"""
n2 = int(input("número: "))
for i in range(n2, -1, -1):
    print(i, end=' , ')

"""Escribir un programa que pregunte al usuario una 
cantidad a invertir, el interés anual y el número de
años y muestre por pantalla el capital obtenido en la 
inversión cada año que dura la inversión"""
cantidad = float(input("ponga la cantidad: "))
interes = float(input("ponga el interés: "))
anios = int(input("ponga los años: "))

for i in range(anios):
    cantidad *= 1 + interes/100
    print("Capital tras "+str(i+1) + " años: " +str(round(cantidad, 2)))

"""Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo, de altura
el número introducido"""
n3 = int(input("escriba el número: "))
for i in range(n3):
    for j in range(i+1):
        print("*", end="")
    print("")

"""Escribir un programa que muestre por pantalla la tabla 
de multiplicar del 1 al 10"""
# \t se usa para simular tablas
for i in range(1, 11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("")

"""Escribir un programa que pida al usuaroi un número
entero y muestre por pantalla un triángulo rectánglo"""
n4 = int(input("Teclee un número: "))
for i in range(1,n4+1,2):
    for j in range(i,0,-2):
        print(j,end="")
    print("")

"""Escribir un programa que almacene la cadena de 
caracteres contraseña en una variable, pregunte al
usuario por la contraseña hasta que introduzca
la contraseña correcta"""
