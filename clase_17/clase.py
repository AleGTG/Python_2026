'''
LEER SU CONTENIDO: r
ABRIR UN ARCHIVO PARA ESCRIBIR EN EL (pisando todo su contenido previo) : w (se usa para MODIFICAR ALGO DEL ARCHIVO)
ABRIR UN ARCHIVO PARA ESCRIBIR EN EL (sin pisar nada; se agrega a lo ultimo): a 
'''

archivo = open(".\clase_17\chau.csv", "r")

contenido = archivo.readlines()



lista_usuarios = []
for linea in archivo:
    print(linea)
    print("-----------")
    palabra = ""
    sub_lista = []
    for letra in linea:
        print(letra)
        if letra != "," and letra != "\n":
            palabra += letra
        else:
            sub_lista.append(palabra)
            palabra = ""
    lista_usuarios.append(sub_lista)
archivo.close()

for i in range(len(lista_usuarios)):
    print(lista_usuarios[i])
    print("----------------")



user_nuevo = [3,"lionel", "Messi", "Argentina", "21345672"]

for i in range(len(user_nuevo)-1):
    user_nuevo[i] = user_nuevo[i] + ","

archivo = open(".\clase_17\chau.csv", "a")

archivo.write("\n")
archivo.writelines(user_nuevo)

archivo.close()


print(lista_usuarios)
print("-------------")
lista_usuarios.pop(1)
# print(lista_usuarios)

for i in range(len(lista_usuarios)):
    for j in range(len(lista_usuarios[i])-1):
        lista_usuarios[i][j] = lista_usuarios[i][j] + ","

print(lista_usuarios)

archivo = open(".\clase_17\chau.csv", "a")

for i in range(len(lista_usuarios[i])-1):
    archivo.writelines(lista_usuarios[i])
    archivo.write("\n")

archivo.close()