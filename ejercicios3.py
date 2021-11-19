"""Escribir un programa que pregunte el nombre
del usuario en la consola y un número entero
e imprima por pantalla en línas distintas el nombre
del usuario tantas veces como el número introducido"""
#no lo hice yo, estudiar
nombre = input("¿Cómo te llamas?: ")
n = input("Introduce un número entero: ")

print((nombre + "\n") *int(n))

"""Escribir un programa que pregunte el nombre
completo del usuario por consola y después muestre
por pantalla el nombre completo del usuario 3 veces: una con
todas las letras en minúscula, otra con todas las letras
mayúsculas y otra solo con la primera letra del nombre
y de los apellidos en mayúscula. El usuario puede introducir
su nombre combinando mayúsculas y minúsculas"""
nombre = input("¿Cuál es su nombre completo? ")

nombre_may = nombre.upper()
nombre_min = nombre.lower()
nombre_nor = nombre.title()

print(nombre_may)
print(nombre_min)
print(nombre_nor)

"""Escribir un programa que pregunte el nombre del
usuario en la consola y después de que el usuario lo
introduzca, muestre por pantalla <nombre> tiene <n> letras,
donde <nombre> es el nombre de usuario en mayúsculas y
<n> es el número de letras que tiene el nombre"""
nombre_u = (input("¿Cuál es su nombre?: ")).upper()
n = len(nombre_u)

print("El nombre: "+nombre_u+" tiene "+str(n)+ " letras.")

"""Los teléfonos de una empresa tienen el siguiente formato
prefijo-número-extensión donde el prefijo es el código del
país +34, y la extensión tiene dos dígitos (por ejemplo,
+34-913724710-56). Escribir un programa que pregunte por un
número de teléfono con este formato y muestre por pantalla
el número de teléfono sin el prefijo y la extensión"""
#estudiarlo, no lo hice yo
telefono = input("Introduce el número de teléfono: ")
print("El número de teléfono es: "+telefono[4:-3])

"""Escribir un programa que pida al usuario que 
introduzca una frase en la consola y muestre por
pantalla la frase invertida"""
#estudiarlo
frase = input("Introduzca una frase chila: ")
frase_len = len(frase)
frase_invertida = frase[frase_len::-1]
print(frase_invertida)

"""Escribir un programa que pida al usuario que 
introduzca una frase en la consola y una vocal,
después que muestre por pantalla la misma frase
pero con la vocal introducida en mayúsucla"""
#Estudiarlo, no lo hice yo
frase2 = input("Otra frase chila: ")
vocal = input("Ahora una vocal: ")
print(frase2.replace(vocal, vocal.upper()))

"""Escribir un programa que pregunte el correo del usuario
en la consola y muestre por pantalla otro correo
electrónico con el mismo nombre (la parte delante del @
pero con dominio ceu.es"""
#estudiar, no lo hice yo
correo = input("Favor de poner su correo: ")
print(correo[:correo.find('@')] + '@ceu.es')

"""Escribir un programa que pregunte por consola el
precio de un producto en dólares con dos decimales
y muestre por pantalla el número de dólares y el número
de céntimos del precio introducido"""
#estudiarlo
precio=input("precio producto: ")
print(precio[:precio.find('.')]+ ' dólares y '+precio[precio.find('.')+1] + ' céntimos.')

"""Escribir un programa que pregunte al usuario la fecha 
de su nacimiento en formato dd/mm/aaaa y mostrar por
pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes
se introduzcan con un solo carácter"""
#estudiarlo
fecha = input("pon la fecha de tu nacimiento: ")
print('Día: '+fecha[:2])
print('Mes: '+fecha[3:5])
print('Año: '+fecha[6:])

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día: ' +dia)
print('Mes: ' +mes)
print('Año: ' +año)

"""Escribir un programa que pregunte por consola por los
productos de una cesta de la compra, separados por comas
y muestre por pantalla cada uno de los productos en 
una línea distinta"""
#Estudiar
productos = input("Introduzca los productos separados por coma: ")
print(productos.replace(',','\n'))

cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))

"""Escribir un programa que pregunte el nombre de un
producto, su precio y un número de unidades y muestre
por pantalla una cadena con el nombre del producto,
seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
el número de unidades con 3 dígitos y el coste total con 8
dígitos enteros y dos decimales"""
#Estudiar
product = input("Favor de teclear un producto: ")
price = float(input("Favor de poner el precio: "))
unit = int(input("Total de unidades: "))

print('{producto}: {unidades:3d} unidades x {precio:9.2f}$ = {total:11.2f}$'.format(producto = product, unidades = unit, precio = price, total = unit * price))

