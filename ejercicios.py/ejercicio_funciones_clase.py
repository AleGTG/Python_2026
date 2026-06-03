# Consigna:
# Un comercio quiere calcular el precio final de una compra de tela. Se ingresan precio por
# metro y cantidad de metros (ambos mayores a 0)
# Se sabe que:
# ● Si el total es mayor a 150 → 10% de descuento
# ● Si es mayor a 500 → 20% de descuento
# ● Si no → sin descuento
# Informar el precio final

validar = 0
precio_final = 0
compra = 0
precio_final = 0


while validar != 0:
    compra = str(input("Desea ingresar una compra? (si/no): "))

    while compra != "si" and compra != "no":
        compra = str(input("Dato invalido!! Desea ingresar una compra? (si/no): "))

    if compra == "si":
        metro = int(input("Ingrese los metros que desea comprar (mayor a 0): "))
        while metro < 0:
            metro = int(input("Dato invalido!! Ingrese los metros que desea comprar (mayor a 0): "))
        cantidad_metros = int(input("Ingrese la cantidad de metros que desea comprar (mayor a 0): "))
        while cantidad_metros < 0:
            cantidad_metros = int(input("Dato invalido!! Ingrese la cantidad de metros que desea comprar (mayor a 0): "))
    else:
        print("Compra finalizada!")

