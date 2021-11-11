"""PRÁCTICA NÚMERO UNO 
supongamos que estas planeando utilizar
tus habilidades de python para construir un servicio
de red social. Decides hostear tu aplicación en
servidores corriendo en la nube. Eliges un proveedor de hosts
que cobra $0.51 por hora. Lanzarás tu producto utilizando un
servidor and quieres saber cuánto costará que opere por día
y por mes
Cuanto costará que un servidor corra por día?
cuánto costará que un servidor corra por mes?"""

costo_hora = 0.51
costo_dia = costo_hora * 24
costo_mes = costo_dia * 30
print("El costo por día es: " +str(costo_dia))
print("El costo por mes es: " +str(costo_mes))

"""PRÁCTICA NÚMERO DOS
basados en el ejemplo pasado, asumamos que has ahorrado
$918 para encontrar tu nueva aventura. Te preguntas cuántos
días puedes mantener un servidor corriendo antes de que tu dinero
se acabe. Claro, esperas que tu red social se vuelva popular y 
que requiera 20 servidores para poder mantener la demanda. 
cuanto costará operar a ese punto?"""
#cuanto costara que opere un servidor por día?
print("El costo por día es de: " +str(costo_dia))
#cuanto costará que opere un servidor por mes?
print("El costo por mes es de: "+str(costo_mes))
#cuanto costará que opere 20 servidores por un mes?
costo_servers = 0.51 * 20
costo_servers_dia = costo_servers * 24
costo_servers_mes = costo_servers_dia * 30
print("El costo por 20 servidores en un mes es de: "+str(costo_servers_mes))
#cuantos días puedo operar un servidor con $918?
server_hora = 918/0.51
total = server_hora / 24
print("Los días total son: "+str(total))