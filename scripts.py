# Consigna:
# Un comercio quiere calcular el precio final de una compra de tela. Se ingresan precio por
# metro y cantidad de metros (ambos mayores a 0)
# Se sabe que:
# ● Si el total es mayor a 150 → 10% de descuento
# ● Si es mayor a 500 → 20% de descuento
# ● Si no → sin descuento
# Informar el precio final


# def validar_numero (numero:int)->int:
#     '''
#     docu
#     '''
#     if numero > 0:
#         return numero
#     else:
#         numero = validar_numero(int(input("Error!!! Ingrese su numero: ")))
#         return numero

def calcular_descuento (numero_1:int, numero_2)->int:
    '''
    docu
    '''
    total = numero_1 + numero_2
    descuento = 0
    if total > 500:
        descuento = total * 0.20
        return descuento
    elif total > 150:
        descuento = total * 0.10
        return descuento
    else:
        return descuento
    
    
def calcular_precio_final (numero_1:int, numero_2)->int:
    '''
    docu
    '''
    total = numero_1 + numero_2
    total_final = total - descuento
    return total_final

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))
descuento = calcular_descuento(numero_1, numero_2)
precio_final = calcular_precio_final(numero_1, numero_2)
print(descuento)
print(precio_final)

#C:/Users/guerr/OneDrive/Desktop/parcial_2/dragon_ball.json


