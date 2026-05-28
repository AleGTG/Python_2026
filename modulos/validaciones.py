def determinar_texto (string:str)->bool:
    '''
    Brief: recorre un string para valida que este
      contenga letras y espacios mediante el codigo ASCII
        

    string: string el cual sera recorrido y validado

    return: retorna true si el string contiene solo
      letras y espacios y false en caso contrario
    '''

    if len(string) == 0:
        return False

    bandera = False

    for i in range (len(string)):
        texto = ord(string[i])

        mayuscula = texto >= 65 and texto <= 90
        minuscula = texto >= 97 and texto <= 122
        espacio = texto == 32

        if mayuscula == True or minuscula == True:
            bandera = True

        if mayuscula == False and minuscula == False and espacio == False:
            return False

    return bandera


def determinar_numero(string:str)->bool:
    '''
    Brief: recorre un string y valida que este
        contenga solamente numeros mediante codigo ASCII

    string: string que sera recorrido y validado

    Return: retorna true si el string contiene solo
        numeros y false en caso contrario
    '''

    if len(string) == 0:
        return False

    for i in range(len(string)):

        numero = ord(string[i])

        if numero < 48 or numero > 57:
            return False

    return True

def determinar_float(string:str)->bool:
    '''
    Brief: recorre un string y valida
        que represente un numero flotante

    string: string que sera recorrido

    Return: retorna true si el string es
        un float valido y false en caso contrario
    '''

    if len(string) == 0:
        return False

    punto = 0
    contiene_numero = False

    for i in range(len(string)):

        if string[i] == ".":
            punto += 1

        else:

            numero = ord(string[i])

            if numero < 48 or numero > 57:
                return False

            contiene_numero = True

    if punto > 1:
        return False

    return contiene_numero

def eliminar_espacios_repetidos(string:str)->str:
    '''
    Brief: Recorre un string y elimina los espacios
            repetidos consecutivos

    string: string que sera recorrido y comparado con espacios

    return: retorna el string sin espacios repetidos consecutivamente
    '''

    if len(string) == 0:
        return ""

    resultado = string[0]

    for i in range(1, len(string)):
        if string[i] != " " or string[i-1] != " ":
            resultado += string[i]

    return resultado

def validar_ingreso_rango(min:int, max:int, mensaje:str)->int:
    '''
    Brief: le pide al usuario que ingrese un entero y valida que
      este en el rango especificado y lo valida segun el rango

    min: entero que nos servira para saber el minimo del rango

    max: entero que nos servira para saber el maximo del rango

    mensaje: texto que nos muestra al pedir el entero

    return: retorna el entero validado dentro de rango
    '''

    opciones = int(input(mensaje + f"({min}-{max}): "))
    while opciones < min or opciones > max:
        opciones = int(input(f"ERROR!!!: {mensaje}"))
    return opciones