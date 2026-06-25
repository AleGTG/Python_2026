#PARADIGMA FUNCIONAL



'''
funciones ciudadano de primera clase:
    X -si las funciones se pueden asignar a variables
    X -si las podes pasar como parametro a otra funcion
    -si en una funcion con return el return puede ser otra funcion
'''

# bool, string, int, float
# list, tupla, dict, set
# funcion

# def promedio(lista:list):
#     acumulador = 0
#     for i in range(len(lista)):
#         acumulador += lista[i]
#     return acumulador / len(lista)

# def suma(a,b):
#     return a+b

# def resta(a,b):
#     return a-b

# def multiplicacion (a,b):
#     return a*b

# calculadora = [suma, resta, multiplicacion]
# calculadora_dict = {
#     "funcion_suma" : suma,
#     "funciona_resta" : resta
# }
# print(calculadora[1](1,2))

# def funcion_superior (funcion:callable, lista:list):
#     acumulador = 0
#     for elemento in lista:
#         acumulador = funcion(acumulador, elemento)
#     print(acumulador)

# def operacion (a,b,funcion):
#     return funcion(a,b)

# operacion(7,1,resta)

# lista = [1,2,3,4,555,6,766,12]
# funcion_superior(suma, lista) # se le llama un funcion call back ( cuando le pasas por parametro un
                                        # afuncion a otra funcion)

# variable_suma = suma # sin parentesis le pasas la direccion de memoria
# resultado = variable_suma(2,5) # con pararentesis le pasa el retorno de la funcion (la estas llamando)
# print(resultado)

# funcion_promedio = promedio # guardamos la direccion en memoria de la funcion
# funcion_promedio(lista) # la funcion es una estrutura y no un tipo de dato

# lista_funciones = [funcion_promedio,variable_suma ]


proyecto = {
    "presupuesto" : 1000000,
    "impacto_esperado" : 20,
    "duracion_estimada" : 3,
    "miembro" : ["mariano", "aguatin", "taiel"],
    "roles" : ["admin", "empleado"]
}


def evaluar_por_presupuesto(proyecto: dict, limite: int=500000)->bool:
    aprobado = False
    if proyecto["presupuesto"] < limite:
        aprobado = True
    return aprobado

def evaluar_por_impacto(proyecto: dict, minimo: int=10)->bool:
    aprobado = False
    if proyecto["impacto_esperado"] < minimo:
        aprobado = True
    return aprobado

def evaluar_por_duracion(proyecto: dict, meses: int=4)->bool:
    aprobado = False
    if proyecto["duracion_estimada"] < meses:
        aprobado = True
    return aprobado

# ASIGNAR FUNCIONES A VARIABLES (O LISTA DE FUNCIONES)
# PASAR FUNCIONES COMO PARAMETRO A OTRAS FUNCIONES

def evaluar_proyecto(proyecto: dict, criterio: callable[[dict, int], bool], parametro: int) -> bool:
    for i in range(len(criterio)):
        booleano = criterio[i](proyecto, parametro)
        if booleano == False:
            print("NO paso")

lista_proyecto = [evaluar_por_presupuesto, evaluar_por_duracion, evaluar_por_impacto]
evaluar_proyecto(proyecto, lista_proyecto, 50)