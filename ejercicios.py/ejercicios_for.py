# Al finalizar, informar:
# Enunciado 1:
# Realizar un programa que solicite al usuario ingresar 10 números enteros.
#  Luego, el programa debe:
# Mostrar la suma total de los números ingresados. 
# Informar cuántos números son pares. 
# Indicar cuál fue el número mayor.

# Enunciado 2:
# Realizar un programa que pida al usuario un número entero positivo.
#  Luego, utilizando un for, mostrar:
# Todos los números desde 1 hasta ese número. 
# La suma de todos esos números. 
# El promedio de los números mostrados

# Enunciado 3:
# Realizar un programa que solicite al usuario ingresar 5 números enteros (uno por uno).
# Por cada número ingresado, el programa debe:
# Determinar si es positivo, negativo o cero. 
# Contar cuántos números positivos, negativos y ceros se ingresaron.
# La cantidad de números positivos. 
# La cantidad de números negativos. 
# La cantidad de ceros. 
# El promedio de los números positivos.


'''
contador_numero = 0
contador_par = 0
total_suma = 0

while contador_numero < 10:
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        contador_par = contador_par + 1
    total_suma += numero
    if contador_numero == 0 or numero > numero_max:
        numero_max = numero
    contador_numero = contador_numero + 1

print(f"La suma total de los nuemros ingresasdos fue: {total_suma}")
print(f"La cantiadd de numeros pares son: {contador_par}")
print(f"El numero mayor es: {numero_max}")
'''

'''
numero = 0
validacion_num = 0

while validacion_num == 0:
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero >= 0:
        validacion_num = validacion_num + 1
    else:
        print("No puede ingresar un numero negativo")

suma = 0

for i in range(0, numero + 1):
    suma += i
    print(i)

promedio = suma / numero
 
print(f"La suma e todos los numeros es: {suma}")
print(f"El promedio es: {promedio}")
'''

cont_numeros = 0
cont_positivos = 0
cont_negativos = 0
cont_ceros = 0
total_suma = 0

while cont_numeros < 5:
    numero = int(input("Ingrese 5 numeros: "))

    if numero > 0:
        cont_positivos = cont_positivos + 1
        total_suma += numero
    elif numero < 0:
        cont_negativos = cont_negativos + 1
    else:
        cont_ceros = cont_ceros + 1
    cont_numeros = cont_numeros + 1


promedio = total_suma / cont_positivos

print(f"La cantidad de numeros positivos ingresada es: {cont_positivos}")
print(f"La cantidad de numeros negativos ingresada es: {cont_negativos}")
print(f"La cantidad de ceros ingresados fueron: {cont_ceros}")

if promedio > 0:
    print(f"El promedio de los nuemros positivos es: {promedio}")
else:
    print("No hay numeros validos para sacar el promedio")

