# FUNCIONES RECURSIVIDAD 

#nota 1 +  nota 2 + nota 3

# def bucles(num:int):
#     '''
#     descripcion:
#     parametro:
#     retorno:
#     '''
#     print("oda :P")
#     bucles()

# bucles("diffosa") wasssa

# numero = int(input("Ingrese un numero: "))

# while numero != -1:
#     print(numero)
#     numero = numero - 1

# for i in range(numero, -1, -1):
#     print(i)

# PASA MANOS DIRECTO (el retorno el de la ultima funcion en apilarse no se modifica)
# def for_decreciente():
#     '''
#     yhea
#     '''

#     if numero > -1:
#         numero = numero - 1
#         for_decreciente(numero)


# v = for_decreciente(numero = int(input("Ingrese un numero: ")))
# for_decreciente(v)
# for_decreciente(numero = int(input("Ingrese un numero: ")))#es lo mismo que el de arriba basicamente


# EL RETORNO SE VA MOIFICANDO
# def sacar_factorial(numero_1:int, numero_2:int):
#     '''
#     docu
#     '''

#     if numero_2 >= 2:
#         numero_2 = numero_2 - 1
#         numero_1 = numero_1 * numero_2
#         sacar_factorial(numero_1, numero_2)


#     print("se resolvio la funion")



# numero = int(input("Ingrese un numero para sacarle el factorial: "))
# numero_2 = numero
# sacar_factorial(numero, numero_2)

#hay 2 tipos de pasa manos directo (el retorno el de la ultima funcion en apilarse no se modifica)
#el retorno se va modificando


def calcular_fibonacci (numero:int):
    '''
    docu
    ''' 
    if numero == 1:
        numero = numero + 0
        return numero
    elif numero != 0:
        retorno = calcular_fibonacci(numero - 1)
        suma = retorno + numero
        retorno_final = suma

    print("finalment se resolvio el maldito fibonacci")
    return retorno_final


    # for i in range(0, numero+1):
    #     if i < 2:
    #         fibonacci_actual = 1
    #         fibonacci_anterior = 0
    #     else:
    #         fibonacci_siguiente = fibonacci_actual + fibonacci_anterior
    #         fibonacci_anterior = fibonacci_actual
    #         fibonacci_actual = fibonacci_siguiente
    
    return fibonacci_actual
    # if numero_1 >= 1:
    #     numero_2 = numero_1
    #     numero_1 = (numero_1 - 2) + (numero_2 - 3)

    #     return numero_1



numero = int(input("Ingrese un numero: "))
fibo = calcular_fibonacci(numero)
print(fibo)
    
