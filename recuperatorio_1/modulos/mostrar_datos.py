def mostrar_datos_filtrados(lista:list, dato, indice:int)->None:
    '''
    Brief: recorre una lista de listas y mustra los datos 
    llamando a la funcion "ver_lista" solo si la sublista
      coincide con el dato pasado por parametro

    lista: lista de listas la cual sera recorrida

    dato: dato de cualquier tipo el cual nos servira para comparar con la sublista

    indice: entero que nos servira para ubicar el sub-indice
    '''

    for i in range(len(lista)):
        if lista[i][indice] == dato:
            ver_lista(lista[i])

def mostrar_lista(lista:list)->None:
    '''
    Brief: recorre una lista llamando
     a la funcion "ver_lista" para mostrar cada elemento

    lista: lista que sera recorrida y 
        cuyos elementos seran mostrados
    '''

    for i in range(len(lista)):
        ver_lista(lista[i])


def ver_lista_unica (lista:list, indice:int)->None:
    '''
    Brief: muestra una sola sub-lista de forma amena para el usuario

    lista: lista de listas en la que se mostrara la sub-lista inicada

    indice: entero que nos sevira de indice para mostrar la sublista indicada
    '''
    print("\n"
        "Nombre:", lista[indice][0], "\n",
        "Tipo:", lista[indice][1], "\n",
        "Altura:", lista[indice][2], "\n",
        "Peso:", lista[indice][3], "\n",
        "Nivel:", lista[indice][4], "\n",
        "Fuerza de Ataque:", lista[indice][5], "\n", 
        "Region:", lista[indice][6], "\n")
    
def ver_lista(lista:list)->None:
    '''
    Brief: muestra por pantalla los datos de 
    una lista de forma amena para el usuario

    lista: lista la cual se muetran los datos
    '''
    print("\n"
        "Nombre:", lista[0], "\n",
        "Tipo:", lista[1], "\n",
        "Altura:", lista[2], "\n",
        "Peso:", lista[3], "\n",
        "Nivel:", lista[4], "\n",
        "Fuerza de Ataque:", lista[5], "\n", 
        "Region:", lista[6], "\n")
    
def ver_dato_exacto(lista:list, indice:int, subindice:int, mensaje:str)->None:
    '''
    brief: muestra solo un elemento exacto de una sublista dentro de una lista de listas

    lista: lista de listas en la que buscaremos el elemento

    indice: entero que nos servira para saber la posicion de la sub-lista

    subindice: entero que nos servira para identificar la posicion del elemento en la sub-lista

    mensaje: mensaje generico para mostar el elemento
    '''
    print("\n"f"{mensaje} {lista[indice][subindice]} ""\n")
    