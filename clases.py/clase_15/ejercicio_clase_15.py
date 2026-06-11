from jugadores import jugadores

def ordenar(lista:list, key):

    for i in range(len(lista) -1):
        for j in range(i + 1, len(lista)):
            if lista[i][key] > lista[j][key]:

                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def mostrar_lista(lista:list, key:str):
    for elemento in lista:

        if type(elemento) == dict:
            mostrar_diccionario(elemento)

        else:
            print(f"{key} : {elemento}")


def mostrar_diccionario(diccionario:dict):
    for clave in diccionario:
        if type(diccionario[clave]) == dict:
            mostrar_diccionario(diccionario[clave])

        elif type(diccionario[clave]) == list:
            print(f"{clave}: ")
            mostrar_lista(diccionario[clave], clave)

        else:
            print(f"{clave}: {diccionario[clave]}")

def mostrar_jugadores (lista:list):
    for jugador in lista:
        mostrar_diccionario(jugador)
        print("\n ---------------------------")

def calcular_promedio_generico(lista:list):
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    return acumulador / len(lista)

def calcular_promedio(lista:list):
    flag = False
    for i in range(len(lista)):
        lista_calificaciones = lista[i]["calificaciones"]

        promedio = calcular_promedio(lista_calificaciones)
        if flag == False or promedio > mayor_promedio:
            flag = True
            mayor_promedio = promedio
            indice_mayor = lista[i]
    return indice_mayor

def buscar_grupos (lista:list):
    for i in range(len(lista)):
        grupos = lista[i]["grupos"]
        for grupo in grupos:
            if grupo["nombre"] == "titulares":
                print(lista[i]["nombre"])


jugadores_1 = [
    {
        "numero": 10,
        "nombre": "Lionel",
        "apellido": "Messi",
        "edad": 39,
        "calificaciones": [10, 9, 10], # de los ultimos partidos, como jugo
        "equipo": {"club": "Inter Miami", "pais": "Estados Unidos"},
        "grupos": [
            {"nombre": "Titulares", "descripcion": "Jugadores habituales del once inicial"},
            {"nombre": "Capitanes", "descripcion": "Referentes del equipo"}
        ],
        "posicion": "Delantero"
    },
    {
        "numero": 22,
        "nombre": "Lautaro",
        "apellido": "Martinez",
        "edad": 29,
        "calificaciones": [9, 8, 10],
        "equipo": {"club": "Inter", "pais": "Italia"},
        "grupos": [
            {"nombre": "Titulares", "descripcion": "Jugadores habituales del once inicial"}
        ],
        "posicion": "Delantero"
    },
]


mostrar_jugadores(jugadores_1)

