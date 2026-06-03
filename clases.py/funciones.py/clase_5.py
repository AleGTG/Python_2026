

                    #recomedacion de tipos de datos str/int/bool
                    #parametros formales
def saludar (nombre:str)->str:

    # print(nombre)
    # print("Hola soy ale")
    print(f"Hola me llamo {nombre}")
    # total = nombre + 1
    # print(total)

#los parametros por poscion
def suma_dos_numeros (numero_1:int, numero_2:int)->int:
    '''
    Sumar dos numeros enteros

    args:

        numero_1 (int): el primer numero
        numero_2 (int): el segundo numero

    return:

        int : El resultado de la suma de dos numeros

    '''
    total = numero_1 + numero_2 #si la variable aparece media difuminada seria
    #                            una variable local que solo se ejecuta dentro de la funcion
    return total

def mostrar_resultado (resultado):#nombre de fantasia

    print(f"El resultado es: {resultado}")
    
#todo lo que se decclara afuera de las funciones son variables goblales

#los parametros por poscion
# suma_dos_numeros(3, 6) valor real
#parametros no posicionales
# resultado = suma_dos_numeros(numero_2=6, numero_1=2)

# mostrar_resultado(resultado)

# # saludar(1)
# nombre = "naan"
# saludar(nombre)
# saludar("jose")
# saludar("ale") #parametro actual

def sumar (numero_1:int, numero_2:int):
    '''
    '''
    total = numero_1 + numero_2
    return total

def restar (numero_1:int, numero_2:int)->int:
    '''
    '''
    total = numero_1 - numero_2
    return total

def dividir (numero_1:int, numero_2:int)->int:
    '''
    '''
    total = numero_1 / numero_2
    return  total

def multiplicar (numero_1:int, numero_2:int)->int:
    '''
    '''
    total = numero_1 * numero_2
    return total

def pedir_numero (mensaje:str):
    '''
    '''
    mensaje = int(input("Ingrese el primer numero: "))
    return mensaje
operacion = 0

while operacion != 0:
    print("""
        
        Elegi una operacion:
          
          1- sumar
          2- restar
          3- dividir
          4- multiplicar
          5- salir
    """)

    while operacion <= 0 or operacion > 5:
        operacion = int(input("Elegi una operacion: "))

        if operacion != 5:
            #vamos viendo que operacion eleguio

            numero_1 = int(input("Ingresa el primer numero: "))
            numero_2 = int(input("Ingresa el segundo numero: "))

            if operacion == 1:
                resultado = sumar(numero_1, numero_2)

            elif operacion == 2:
                resultado = restar(numero_1, numero_2)

            elif operacion == 3:
                resultado = dividir(numero_1, numero_2)

            else:
                resultado = multiplicar(numero_1, numero_2)

            print(f"El resultado es: {resultado}")
            operacion = 0



            
