condicion = 20 > 10

while 20 > 10:
    pass

'''a = 1

while a < 10:
    print(a)''' #bucle infinito


a = 1
b = 10

while a < 10:
    print(a)
    b += 145
    #b = b + 145

    a += 1 #acumulador

print(b)
print("oda")

'''
contador_estudiantes = 0
acumulador_nota = 0

while contador_estudiantes != 10:
    estudiante = input("ingrese su nombre estudainte: ")
    nota = int(input("que nota te sacaste en el examen?: "))

    acumulador_nota + nota #acumulador
    contador_estudiantes = contador_estudiantes + 1 #contador'''
'''
nota = input("Nota: ")

while nota != "FIN": #promedios
    nota = input("Nota: ")'''

#maximos y minimos

# (ej) identificar quien pateo mas lejos en mts

#cuando no sabemos cual es el limite INFERIOR en nuetro conjunto -> flag


contador_jugadores = 0
#distancia_maxima = 0 Solo inicializar el numero solo si se sabe el nuemro maximo
flag = True    # (true, false)

while contador_jugadores < 10:
    distancia = int(input("A que distancia pateaste: "))

    if flag == True:   #sirve para identificar un valor
        flag = False   #la bandera en la segunda iteracion ya no va a true por lo tanto no entra en el primer if
        distancia_maxima = distancia

    elif distancia > distancia_maxima:
        distancia_maxima = distancia

    contador_jugadores = contador_jugadores + 1

# el contador siempre suma la misma cantidad
# el acumulador varia en la cantidad

