#VALIDACIONES
#(entre 10 y 100 kilos)
peso = int(input("Ingrese el peso: "))

while peso < 10 or peso > 100:
    peso = int(input("Ingrese el peso: "))

print(peso)

################################################
#FOR

#if (while , for)

# contador = 0
# while contador < 10:
#     print(contador)
#     contador = contador + 2

# variable = range(10) # 1 -> (0-9) hasta
# variable = range(1, 11) # 1 -> (0-9) desde-hasta
# variable = range(11, 1, -1) # 1 -> () desde-hasta-"de cuanto en cuanto"
# # (1-10)
# print(variable) 

# 0,1,2,3,4,5,6,7,8,9

# for i in range(1,11):
# #    #for j in range(10):
#     print(i) # variable de control (nos controla el rango numerico del for)
# #    print("hola")

#print("sali del for")
## i muere :c

# el for se ejecuta mediante una lista de numeros
# while se ejecuta con un booleano

# for i in range(10):
#     print(i)
#     if i == 2:
#         continue # ingnora/salte
#         print("hola") # ingnorado :c
#     nombre = input("nombre: ")
#     edad = int(input("edad: "))

#     if i == "DARIO BENEDETTI":
#         break

# for i in range(5):
#     print(i + 1) #variable de control mas 1 unindad

for i in range(1, 6):
    print(i)
    print("INICIO DE BUCLE")
    for j in range(10, 16):
        print(j)
    print("FIN DEL BUCLE")


