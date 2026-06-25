# lista = [1,2,3,4]
# n = int(input("Agre un elemento a la lista: "))
# lista[0] = n

# print(lista)

# import os

# var = os.getcwd() # des que jerarquia de carpeta abrirte el visual studio code (str)
# print("--------------")
# # print(os.getcwd()) # donde esta el entry point
# print(var)
# print("--------------")

# contenido = archivo.readli()
# contenido_listas = archivo.readlines()
# print(contenido_listas)

# archivo.write("\nCHAU MUNDO")
# archivo.writelines("hola", "division", "213")



'''
LEER SU CONTENIDO: r
ABRIR UN ARCHIVO PARA ESCRIBIR EN EL (pisando todo su contenido previo) : w
ABRIR UN ARCHIVO PARA ESCRIBIR EN EL (sin pisar nada; se agrega a lo ultimo): a
'''

archivo = open(".\clase_16\chau.csv", "a")


archivo.close()# cierra el archivo

# with open(".\clase_16\chau.txt", "") as archivo: #cuando estas fuera del whit open se te cierra solo
#     # haces tus cosas
#     pass