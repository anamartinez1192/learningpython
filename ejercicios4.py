"""Escribir un programa que pregunte al usuario su 
edad y muestre por pantalla si es mayor de edad o no"""
edad = int(input("Favor de teclear su edad: "))
if edad < 18:
    print("Usted es menor de edad!!!")
else:
    print("Usted ya es mayor de edad :)")

"""Escribir un programa que almacene la cadena de
caracteres contraseña en una variable, pregunte al usuario
por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la
variable, sin tener en cuenta mayúsculas y minúsculas"""
contra1 = 'cocomelon'
contra2 = input("Favor de introducir contraseña: ")

if contra1 == contra2:
    print("las contraseñas coinciden :)")
else:
    print("sorry, intenta de nuevo, bro :(")

"""Escribir un programa que pida al usuario dos números
y muestre por pantalla su división. Si el divisor
es 0, el programa debe mostrar un error"""

n1 = int(input("Favor de teclear un número: "))
n2 = int(input("Favor de teclear el segundo número: "))
if n2 == 0:
    print("Error, favor de teclear un número diferente a 0 :(")
else:
    print("El resultado es: "+str(n1/n2))

"""Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es par o impar"""
numero = int(input("introduzca el número: "))
if (numero%2) == 0:
    print("el número es par :)")
else:
    print("el número no es par :(")

"""Para tributar un determinado impuesto, se debe ser
mayor de 16 años y tener unos ingresos iguales o
superiores a 10000$ mensuales. Escribir un programa
que pregunte al usuario su edad y sus ingresos y muestre
por pantalla si el usuario tiene que tributar o no"""
edad = int(input("Teclear edad: "))
ingresos = int(input("Teclear ingresos: "))

if edad > 16 and ingresos > 10000:
    print("tienes que tributar, bro")
else:
    print("estás chavo aún o muy pobre")

"""Los alumnos de un curso se han dividido en dos grupos
A y B de acuerdo al sexo y el nombre. El grupo A está
formado por las mujeres con un nombre anterior a la M y los
nombres con un nombre posterior a la N y el grupo B por el 
resto. Escribir un programa que pregunte al usuario su 
nombre y sexo y muestre por pantalla a que grupo corresponde"""
#Estudiar y corregir este programa
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

"""Escribir un programa que pregunte al usuario su renta
anual y muestre por pantalla el tipo
impositivo que le corresponde"""
renta = int(input("renta anual: "))
if renta < 10000:
    print("tipo impositivo del 5%")
elif renta >= 10000 and renta <= 20000:
    print("tipo impositivo del 15%")
elif renta > 20000 and renta <= 35000:
    print("tipo impositivo del 20%")
elif renta > 35000 and renta <= 60000:
    print("tipo impositivo de 30%")
elif renta > 60000:
    print("tipo impositivo de 60%")

"""Escribir un programa que lea la puntuación del
usuario e indique su nivel de rendimiento, así como
la cantidad de dinero que recibirá el usuario"""
cantidad_dinero = 2400
puntuacion = float(input("Ingrese la puntuación: "))
if puntuacion == 0.0:
    print("Su nivel es INACEPTABLE")
    print("Su dinero a recibir es de: "+str(cantidad_dinero*puntuacion))
elif puntuacion == 0.4:
    print("Su nivel es Aceptable.")
    print("Su dinero a recibir es de: "+str(cantidad_dinero * puntuacion))
elif puntuacion >= 0.6:
    print("Su nivel es MERITORIO!!!")
    print("Su dinero a recibir es de: "+str(cantidad_dinero*puntuacion))

"""Escribir un programa para una empresa que tiene salas
de juegos para todas las edades y quiere calcular
de forma automática el precio que debe colocar a sus
clientes por entrar. El programa debe preguntar al usuario 
la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años, puede entrar gratis, si
tiene entre 4 y 18 años, debe pagar $5 y si es mayor de
18 años, pagará $10"""
edad_cliente = int(input("¿Cuál es su edad?: "))
if edad_cliente < 4:
    print("Tú entras gratis, pequeñín c:")
elif edad_cliente >= 4 and edad_cliente <= 18:
    print("tú tienes que pagar $5 dólares, pibe")
elif edad_cliente > 18:
    print("Grandote, tú pagas $10 dólares")

"""Escribir un programa que pregunte al usuario si quiere
una pizza vegetariana o no y en función de su respuesta,
le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede elegir un ingrediente además de la mozzarella
y el toomate que están en todas las pizzas. Al final, se debe mostrar
por pantalla si la pizza elegida es vegetariana o no y todos
los ingredientes que lleva"""
respuesta = input("¿Desea pizza vegetariana o no vegetariana?: ")
if respuesta == 'vegetariana':
    print("Los ingredientes disponibles son los siguientes: \nPimiento \nTofu")
elif respuesta == 'no vegetariana':
    print("Los ingredientes disponibles son los siguientes: \nPeperoni \nJamón \nSalmón")
else:
    print("Favor de elegir una de las dos opciones")

ingrediente = input("Eliga los ingredientes que desea: ")
print("La pizza que usted eligió es: "+respuesta+ " y los ingredientes son: "+ingrediente)
