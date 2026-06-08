from jugadores import jugadores

def ordenar(lista:list):

    for i in range(len(lista) -1):
        for j in range(i + 1, len(lista)):
            if lista[i]["apellido"] > lista[j]["apellido"]:

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

