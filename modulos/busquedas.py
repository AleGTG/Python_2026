def buscar_indice_dato(lista:list, dato:str, indice:int):
    '''
    Brief: busca el indice de una sublista cuyo valor sea igual
         en el indice indicado con el dato pasado por parametro
    
    lista: lista de listas en la que buscaremos el indice

    dato: dato tipo string con el buscaremos el indice

    indice: indice de tipo entero de cada sublista que sera comparado

    return: retorna el indice de la sublista. si no existe retornara -1
    '''

    for i in range(len(lista)):
        if lista[i][indice] == dato:
            return i
        
    return -1

def comparar_datos(lista:list, indice:int, subindice:int)->int:
    '''
    Brief: recorre un lista de listas y saca el mayor 
        valor segun el sub-indice

    lista: lista de listas que sera recorrida

    indice: indice de tipo entero que nos servira 
        de refencia inicial

    subindice: sub-indice de tipo entero que nos servira para 
            comparar dentro de la sublista

    return: retorna el dato de mayor valor 
            comparado segun el subindice
    '''

    dato = lista[indice][subindice]

    for i in range(1, len(lista)):
        if lista[i][subindice] > dato:
            dato = lista[i][subindice]

    return dato
