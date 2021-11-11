"""Crea un programa que pregunte al usuario que tan
lejos quieren viajar. Si quieren viajar menos que 3 millas,
entonces les dices que camine. Si quieren viajar más
de 3 millas pero menos que 300 millas, diles que manejen.
Si quieren viajar 300 millas o más diles que tomen avión"""

millas = int (input('¿Qué tanto desea viajar?'))

if millas < 3:
    print('Camine, no sea flojo')
elif millas >= 3 and millas < 3000:
    print('Bueno, esta vez puede tomar carro')
elif millas >= 3000:
    print('Ok ok, toma avión')
else:
    print('mejor no viaje')

