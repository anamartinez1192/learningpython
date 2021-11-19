"""escribir un programa que muestre Hola Mundo!"""

print("Hola, Mundo!!!")

"""escribir un programa que almacene la cadena
hola mundo en una variable y luego muestre
por pantalla el contenido de la variable"""

variable = input("escriba: ")
print(variable)

"""escribir un programa que pregunte el nombre del
usuario en la consola y después de que el usuario lo
introduzca, muestre por pantalla la cadena 
Hola <nombre>, donde <nombre> es el que puso el usuario"""

nombre = input("¿Cual es su nombre?: ")
print("Hola, "+nombre+"!!!")

"""escribir un programa que muestre por pantalla
el resultado de la sigiuente operación aritmética"""
#ufff :(

"""Escribir un programa que pregunte al usuario por el número
de horas trabajadas y el coste por hora.
Después mostrar por pantalla la paga que le corresponde"""

horas = float(input("ingrese las horas trabajadas: "))
costo = float(input("ingrese el costo por hora: "))

pago_total = horas * costo

#como redondear un float
print("la paga total es: {0:.2f}".format(pago_total))

"""escribir un programa que lea un entero positivo n
introducido por el usuario y después muestre en pantalla
la suma de todos los enteros desde 1 hasta n."""
#ufff

"""escribir un programa que pida al usuario su peso (kg)
y estatura (m), calcule el índice de masa corporal y
lo almacena en una variable y muestre por pantalla la
frase tu indice de masa corporal es <imc> donde el imc está
calculado redondeado a dos decimales"""

peso = float(input("ingrse su peso: "))
altura = float(input("ingrese su estatura en metros: "))
imc = peso/(altura**2)

print("Tu IMC es: {0:.2f}".format(imc))

"""escribir un programa que pregunte al usuario una
cantidad a invertir, el interés anual 
y el número de años y muestre por pantalla el capital
obtenido de la inversión"""
inversion = int(input("Favor de ingresar la inversión: "))
tasa_interes = int(input("¿Cuál sería la tasa de interés?: "))
no_anios = int(input("¿Cuántos años?: "))
interes = tasa_interes/100

capital = inversion*interes*no_anios

print("Su capital generado es de: "+str(capital))

"""Una juguetería tiene mucho éxito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la empresa
de logística les cobra por peso de cada paquete, así que deben
calcular el peso de los payasos y muñecas que saldrán en cada
paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g.
Escribir un programa que lea el número de payasos y muñecas
vendidos en el último pedido y calcule el peso total del
paquete que será enviado"""
peso_payaso = 112/1000
peso_doll = 75/1000

payasos_total = int(input("¿Cuántos payasos serán?: "))
dolls_total = int(input("¿Cuántas muñecas serán?: "))

payasos = peso_payaso * payasos_total
dolls = peso_doll * dolls_total

total = payasos + dolls

print("El número de payasos a enviar serán de: "+str(payasos_total)+ " y el número de muñecas a enviar será de: "+str(dolls_total)+ " con un peso respectivamente de: "+str(peso_payaso)+ " y "+str(peso_doll)+ " y el peso total del paquete sería de: "+str(total)+ " kilos.")

"""Imagina que acabas de abrir una nueva cuenta de 
ahorros que te ofrece el 4% de interés al año. Estos
ahorros debido a intereses, que no se cobran hasta finales
de año, se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario.
Después, el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y tercer
año. Redondear cada cantidad a dos decimales"""
interes_anio = 4/100
ahorros = float(input("Ingrese la cantidad de ahorros: "))

balance1 = ahorros + (ahorros*interes_anio*1)
balance2 = ahorros + (ahorros*interes_anio*2)
balance3 = ahorros + (ahorros*interes_anio*3)

print("Balance ahorro primer año: {0:.2f}".format(balance1))
print("Balance ahorros segundo año: {0:.2f}".format(balance2))
print("Balance ahorros tercer año: {0:.2f}".format(balance3))

"""Una panadería vende barras de pan a 34.90 cada una. El pan
que no es del día tiene un descuento del 60%. Escribir
un programa que comience leyendo el número de barras
vendidas que no son del día. Después, el programa debe mostrar
el precio habitual de una barra de pan, el descuento
que se le hace por no ser fresca y el coste final total"""
barra_pan = 34.90
descuento = (barra_pan*60)/100

barras = int(input("¿Cuántas barras de pan se están vendiendo?: "))

print("Precio barra de pan: "+str(barra_pan))
print("Descuento a aplicar a cada una: "+str(descuento))
barra_dct = barra_pan - descuento
costo_total = barras * barra_dct
print("Total venta: {0:.2f}".format(costo_total))

