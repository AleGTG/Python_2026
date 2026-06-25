import json

def leer_json ():
    with open("ejercicio_json_en_clase/juegos.json","r") as archivo:
        datos = json.load(archivo)
        return datos

def eliminar_dato (datos):
    nombre_juego = input("Nombre del juego a eliminar: ")
    for i in range(len(datos)):
        if datos[i]["titulo"] == nombre_juego:
            print(f"El juego se elimino ({nombre_juego})")
            datos.pop(i)
            break

def guardar_en_json(datos):
    with open("ejercicio_json_en_clase/juegos.json","w") as archivo:
        json.dump(datos, archivo, indent=4)

lista_dict = leer_json

for i in range(len(lista_dict)):
    print(lista_dict[i])
    print("-.--------------------")

eliminar_dato(lista_dict)
guardar_en_json(lista_dict)