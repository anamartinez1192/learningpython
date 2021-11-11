"""historia corta
había una vez un *perro* al 
que le gusta *correr* y un día tropezó
muy *feo*"""

def get_words():
    """obtener las palabras"""
    noun = str(input('cual es el sustantivo?'))
    verb = str(input('cual es el verbo?'))
    adj = str(input('cual es el adjetivo?'))
    
    return noun, verb, adj

def fills_in(noun, verb, adj):
    """rellenar la historia"""
    print('Habia una vez un {} al que le gusta {} y un día tropezó muy {}'.format(noun, verb, adj))

def display_story():
    get_words()
    fills_in('perro', 'correr', 'feo')

display_story()