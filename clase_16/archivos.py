# lista = [1,2,3,4]
# n = int(input("Agre un elemento a la lista: "))
# lista[0] = n

# print(lista)

import os

var = os.getcwd() # des que jerarquia de carpeta abrirte el visual studio code (str)
print("--------------")
# print(os.getcwd()) # donde esta el entry point
print(var)
print("--------------")

archivo = open(".\clase_16\chau.txt", "w")

archivo.close()# cierra el archivo

for linea in archivo:
    print(linea)