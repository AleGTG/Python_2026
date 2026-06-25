import json
with open("clase_17/archivo.json", "r") as archivo_json:
    datos = json.load(archivo_json)
    print(type(datos))


dict_nuevo = {
    "nombre" : "nicolas",
    "apellido" : "guevara"
}

datos.append(dict_nuevo)

with open("clase_17/rchivo.json", "a") as archivo_json:
    json.dump(dict_nuevo, archivo_json, indent=4)



'''
PARA MODIFICAR O ELIMINAR UN ARCHIVO 

1- Leer el contenido original del archivo y castearlo a un tipo de dato qeu conozca (lista de listas
o listas de diccionarios)

2- A ese dato conocido (lista de listas o lista de diccionario), le hacen el append, el pop, modifican, lo
que quieran

3- Volver a abrir el archivo en modo W (para pisar el contenido original con el nuevo) y guardar ese dato
que modificaron ustedes

'''
