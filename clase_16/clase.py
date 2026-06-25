# copiar por igualdad
lista_ususarios = [
    [1,2,3],
     "agustin",
     "fernando",
     {"hola": "chau"}
]
 # la variable copia tiene otra memoria de direccion original
                                            # solo copia el contenido de la lista original se le llama shallow copy
# lista_ususarios = tuple(lista_ususarios)  # los tipos de datos simple se guardan normal si el tipo de dato es
#                                            sencillo copia el valor solo sirve para una lista de una dimension
                                            # si se encuentra con un elmento complejo copia el id

import copy
# copia_lista_usuarios = copy.deepcopy(lista_ususarios)

# copia_lista_usuarios[0].append(4)

# print(id(lista_ususarios))
# print(id(copia_lista_usuarios))

# print("----------------")
# print(lista_ususarios)
# print(copia_lista_usuarios)

copia_lista_usuarios = lista_ususarios.copy()

# copia_lista_usuarios = []
# for elemento in lista_ususarios:
#     copia_lista_usuarios.append(elemento)
# copia_lista_usuarios = lista_ususarios

# numero = 34
# copia_numero = numero # la variable copia es igual a la variable original en la direccion de memoria
# print(id(numero))
# print(id(copia_numero))

# copia_lista_usuarios.append("Juan")

# print(lista_ususarios)
# print("----------------")
# print(copia_lista_usuarios)

