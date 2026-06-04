from modulos.validaciones import determinar_numero
from modulos.validaciones import determinar_float
from modulos.validaciones import determinar_texto
from modulos.busquedas import buscar_indice_dato
from modulos.validaciones import eliminar_espacios_repetidos



def pedir_entero_positivo(mensaje:str)->int:
    '''
    Brief: pide al usuario que ingrese un entero y 
        valida que sea un numero llamando a la funcion 
        "determinar_numero" y que este sea positivo

    mensaje: mensaje para pedir el numero

    return: retorna el entero positivo validado
    '''

    numero = (input(mensaje))

    while determinar_numero(numero) == False or int(numero) <= 0:
        numero = input(f"Error!!! {mensaje}: ")

    return int(numero)

def pedir_float_positivo(mensaje:str)->float:
    '''
    Brief: pide al usuario que ingrese un float y
    valida que sea un numero llamando a la funcion
    "determinar_float" y que sea positivo

    mensaje: mensaje para pedir el numero

    Return: retorna el float positivo validado
    '''

    numero = (input(mensaje))

    while determinar_float(numero) == False or float(numero) <= 0:
        numero = input(f"Error!!! {mensaje}: ")

    return float(numero)

def pedir_string(mensaje:str)->str:
    '''
    Brief: pide al usuario que ingrese string y valida 
        que esta solo tenga letras y espacios

    mensaje: mensaje con el que se pedira el string

    return: retorna el texto validado
    '''

    texto = input(mensaje)

    texto = eliminar_espacios_repetidos(texto)

    while determinar_texto(texto) == False:
        texto = input(f"Error!!! {mensaje}: ")

    texto = eliminar_espacios_repetidos(texto)

    return texto.capitalize()

def pedir_dato(lista:list, indice:int, mensaje:str)->int:
    '''
    Brief: pide un dato al usuario y busca en la lista mediante 
    la funcion "buscar_indice_dato". si el dato no existe 
    vuelve a pedirlo hasta que sea valido

    lista: lista de listas con la que se buscara el dato

    indice: entero el cual se pasa por parametro a la funcion "buscar_indice_dato"

    mensaje: mensaje de tipo string por el cual se le pedira el dato al usuario

    return: retorna la posicion del dato que estamos buscando
    '''

    dato = input(mensaje).capitalize()
    posicion = buscar_indice_dato(lista, dato, indice)

    while posicion == -1:

        dato = input(f"ERROR!!! {mensaje}").capitalize()
        posicion = buscar_indice_dato(lista, dato, indice)

    return posicion


