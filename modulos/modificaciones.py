from modulos.inputs import pedir_string
from modulos.inputs import pedir_float_positivo
from modulos.inputs import pedir_entero_positivo




def agregar_lista (lista:list, mensaje_inicio:str, mensaje_final:str)->list:
    '''
    Brief: Pide diversos tipos de datos al usuario, crea una sub-lista
      y la agrega a la lista de listas

    lista: lista de listas a la que se agregara la sub-lista

    mensaje_inicio: texto que se mostrara al inicio del mensaje

    mensaje_final: texto que se mostrara al final del mensaje

    return: retorna la nueva sub-lista creada
    '''
    
    nombre = pedir_string(f"\n{mensaje_inicio} el nombre {mensaje_final}: ")

    tipo = pedir_string(f"{mensaje_inicio} el tipo {mensaje_final}: ")

    altura = pedir_float_positivo(f"{mensaje_inicio} la altura {mensaje_final}: ")
    
    peso = pedir_float_positivo(f"{mensaje_inicio} el peso {mensaje_final}: ")
    
    nivel = pedir_entero_positivo(f"{mensaje_inicio} el nivel {mensaje_final}: ")

    fuerza_ataque = pedir_entero_positivo(f"{mensaje_inicio} la fuerza de ataque {mensaje_final}: ")

    region = pedir_string(f"{mensaje_inicio} la region {mensaje_final}: ")

    while region != "Johto" and region != "Kanto" and region != "Sinnoh" and region != "Hoenn" and region != "Kalos":
        region = input(f"Error!!! {mensaje_inicio} la region {mensaje_final}: ").capitalize()

    nuevo_poke = [nombre, tipo, altura, peso, nivel, fuerza_ataque, region]

    lista.append(nuevo_poke)

    return nuevo_poke

def ordenar_lista_descendente(lista:list)->None:
    '''
    Brief: ordena una lista de mayor a menor

    lista: lista de elementos que seran ordenados  
            de forma descendente
    '''

    
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):

            if lista[i] < lista[j]:

                
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista_ascendente(lista:list)->None:
    '''
    Brief: ordena una lista de menor a mayor

    lista: lista de elementos que seran ordenados 
            de forma ascendente
    '''
    
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):

            if lista[i] > lista[j]:

                
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_datos_descendente(lista:list, indice:int)->None:
    '''
    Brief: ordena una lista de listas de mayor a menor

    lista: lista dde listas cuyos elementos que seran 
            ordenados de forma descendente

    indice: entero que sirve para indentificar el sub-indice
    '''
    
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):

            if lista[i][indice] < lista[j][indice]:

                
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def crear_lista_filtrada (lista:list, dato, indice:int)->list:
    '''
    Brief: crea una lista de listas siempre y cuando los datos
         concuerden con el parametro dato

    lista: lista de listas con la que trabajamos

    dato: dato de cualquier tipo el cual servira de filtro

    indice: entero que sirve para identificar el sub-indice

    return: retorna la nueva lista que contiene los datos filtrados
    '''

    lista_nueva = []

    for i in range(len(lista)):
        if lista[i][indice] == dato:
            lista_nueva.append(lista[i])

    return lista_nueva

def eliminar_elemento(lista:list, dato:int):
    '''
    Brief: elimina un elemento de la lista
        utilizando la funcion pop

    lista: lista de listas en la cual se eliminara
             un elemento

    dato: dato de tipo entero el cual servira para idicar
        la posicion del elemento que sera eliminado
    '''

    lista.pop(dato)
