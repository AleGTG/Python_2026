# Realizar un programa que permita mostrar una pirámide de números. 
# Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
# 1
# 12
# 123
# 1234
# 12345

numero = int(input("Ingrese un numero: "))

numero_2 = ""

for i in range(1, numero + 1):
    numero_2 = ""
    for j in range(1, i + 1):
        numero_2 += str(j)


    print (numero_2)
