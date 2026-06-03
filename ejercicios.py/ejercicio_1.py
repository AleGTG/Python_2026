''''Se debe desarrollar un programa que determine qué tipo de beca recibe un
estudiante según diferentes condiciones académicas y económicas.
Tipos de becas posibles:
● Beca completa.
● Media beca.
● Beca con ayuda económica.
● No recibe beca.
Reglas de asignacion:
1. Beca completa si:
- Tiene un promedio mayor o igual a 8,5.
- Sus ingresos son menores a 300000.
- Tiene menos de 18 años.
2. Media Beca si:
- Tiene un promedio entre 7 u 8 y tiene menos de 18 años.
O bien:
- Tiene promedio mayor o igual a 8.5 y sus ingresos familiares son mayores o
iguales a 300000.
3.
- Los ingresos familiares son menores a 200000.
- El promedio es mayor o igual a 6.
Nota: Si el estudiante tiene más de 18 años, no puede obtener esta beca.
4. No recibe beca si:
- No cumple con ninguna de las condiciones anteriores.
Datos a solicitar:
● Edad (entero).
● Ingresos familiares (entero).
● Materias aprobadas (entero).
● Total de materias (entero)
'''


edad = int(input("ingrese su edad: "))
ingresos = int(input("ingrese sus ingresos familiares: "))
materias_apro = int(input("ingrese sus materias aprobadas: "))
materias_total = int(input("ingrese el total de materias: "))
promedio = materias_apro / materias_total * 10
beca = "no tiene beca"

print(promedio)

'''if edad < 18:
    if promedio >= 8.5 and ingresos < 300000:
        print("puede tener la beca completa")
    elif promedio >= 7 and promedio <= 8 or promedio >= 8.5 and ingresos >= 300000:
        print("puede tener la beca media")
    elif ingresos < 200000 and promedio <= 6:
        print("puede tener la beca con ayuda economica")
else:
    print("no cumple con ninguna de las condiciones anteriores")'''

if edad < 18:
    if promedio >= 6:
        if ingresos < 300000 and promedio >= 8.5:
            print("completa")
        elif promedio >= 7 and promedio <= 8:
            print("media")
        elif promedio >= 8.5 and ingresos >= 300000:
            print("media")
    elif ingresos < 200000:
        print("economica")
else:
    print("no condiciones")     
         #ESTA NOOOOOO



