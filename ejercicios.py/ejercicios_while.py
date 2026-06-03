# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# -Apellido
# -Edad, entre 18 y 90 años inclusive.
# -Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# -Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla


apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
est_civil = str(input("Ingrese su estado civil: "))
legajo = int(input("Ingrese su numero de legajo: "))

# while apellido >= "a" or apellido <= "z":
#     apellido = (input("Su apellido es invalido ingrese su apellido nuevamente: "))
    
while edad < 18 or edad > 90:
    edad = int(input("Edad invalida, Ingrese su edad nuevamente: "))

while est_civil != "soltero/a" and est_civil != "casado/a" and est_civil != "divoriado/a" and est_civil != "viudo/a":
    est_civil = str(input("Estado civil no valido porfavor ingrese su estado civil devuelta: "))

while legajo < 1000 or legajo > 9999:
    legajo = int(input("Legajo invalido ingrese su legajo nuevamente: "))

print(f"El apellido ingresado es: {apellido}")
print(f"La edad ingresada es: {edad}")
print(f"Su estado civil es: {est_civil}")
print(f"Su numero de legajo es: {legajo}")


# Realizar un programa que permita que el usuario ingrese todos 
# los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

# contador_numeros = 0
# suma_positiva = 0
# suma_negativa = 0
# cont_negativa = 0
# cont_positivo = 0
# validacion_programa = 0
# numero_max = 0

# while validacion_programa == 0:
#     numero_valid = (input("Desea ingresar un numero (si/no): "))

#     if numero_valid == "si":
#         numero = int(input("Ingrese su numero: "))
#         if numero >= 0:
#             suma_positiva += numero
#             cont_positivo = cont_positivo + 1
#             numero_positivo = numero
#             if numero_positivo > numero_max:
#                 numero_max = numero_positivo
#         if numero <= 0:
#             suma_negativa += numero
#             cont_negativa = cont_negativa + 1
#         contador_numeros = contador_numeros + 1

#     elif numero_valid == "no":
#         print("Fin de programa")
#         validacion_programa = validacion_programa + 1
#     else:
#         numero_valid = (input("Numero invalido ingrese un numero nuevamente: "))

# promedio = suma_positiva / cont_positivo

# porcentaje_negativo = (cont_negativa * 100) / contador_numeros


# print("/////////////////////////////////////////////////////////////////\n")
# print(f"La suma de los positivos es: {suma_positiva}")
# print(f"La suma de los negativos es: {suma_negativa}")
# print(f"La cantidad de numeros negativos son: {cont_negativa}")
# print(f"El pormedio de los positivos es: {promedio}")
# print(f"El numero positivo mas grande es: {numero_max}")
# print(f"El porcentaje de los numeros negativos ingresados es: {porcentaje_negativo}%")

