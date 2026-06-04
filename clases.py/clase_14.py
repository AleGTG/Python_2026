# entero = 34
# string = "2223"

# lista = ["Nico", 33]

# diccionario = {
#     "nombre": "Nico",
#     "edad": 33
# }

# print(lista[0])
# print(diccionario["nombre"])

user_list = [
    1, 
    "nicolas",
    "garcia",
    "argentina",
    37564333
]
#     0-id | 1-nombre | 2-apaellido | 3-nacionalidad | 4-dni



def agregar_usuario (diccionario):
    # tupla -> lista que no se puede modificar; asi como la defino, va a quedar
    lista = []
    for variable in diccionario:
        tupla = (variable, diccionario[variable])
        lista.append(tupla)
    key = input("Ingrese el key: ")
    value = input("Ingrese el value: ")

    tupla_keyvalue = (key,value)

    print(lista)
    lista.append(tupla_keyvalue)
    lista = dict(lista)
    print(lista)


def agregar_dato_diccionario(diccionario:dict, key=-1):
    if key == -1:
        key = input("Ingrese el key: ")

    bandera = verificar_key(diccionario, key)

    # for clave in diccionario:
    #     if clave == key:
    #         bandera == True

    if bandera == False:
        value = input(f"Ingrese {key}: ")
        diccionario[key] = value
    else:
        print("ya existe la key que se intenta agregar")


# l = [
#     ("a", 1),
#     ("b", 2),
#     ("c", 3)
# ]

# l = dict(l)

def eliminar_dict (diccionario):
    lista = []
    delete_key = input("Key a eliminar: ")
    for key in diccionario:
        if key != delete_key:
            tupla = (key, diccionario[key])
            lista.append(tupla)
    lista = dict(lista)

    print(lista)


def eliminar_dict_facil(diccionario, msj:str):
    delete_key = input(msj)

    retorno = True


    encontro = verificar_key(diccionario, delete_key)
    if encontro == True:
        diccionario.pop(delete_key)
    else:
        retorno = False

    return retorno



def verificar_key (diccionario:dict, key):
    bandera = False
    for clave in diccionario:
        if clave == key:
            bandera = True
    return bandera

user_dict = {
    "id": 1,
    "nombre": "nicolas",
    "apellido": "garcia",
    "nacinalidad": "argentina",
    "dni": 37564333,
}

lista_usuario = [
    user_dict
]

def agregar (lista:list, lista_keys):

    diccionario = {"id" : len(lista)+1}
    
    for i in range(len(lista_keys)):
        agregar_dato_diccionario(diccionario, lista_keys[i])
    
    lista.append(diccionario)

agregar(lista_usuario)








# lista_todo = diccionario.items() # te devuleve una lista con las tuplas
# print(list(lista_todo))

# for elemento in diccionario.values: # da el de los values
#     print(elemento)

# for key in diccionario: # da el de las keys
#     print(f"{key} -> {diccionario[key]}")

# for i in range(len(lista_todo)):
#     print(lista_todo[i])

# lista_keys = diccionario.keys() # lista con solo las keys de una diccionario
# print(list(lista_keys))

# lista_values = diccionario.values() # lista con solo los values de una diccionario
# print(list(lista_values))


'''
diccionario[key] = value # agregar
diccionario.pop(delete_key) # eliminar

RECORREMOS DICCIONARIO CON FOREACH CLASICO
variable control -> keys
'''