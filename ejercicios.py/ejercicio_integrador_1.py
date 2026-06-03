# Consigna 1
# Nos ingresan una cantidad indeterminada de estadías de vacaciones, validando los datos
# ingresados:
# nombre del titular ,
# lugar ( “Puerto Madryn”, “Villa Gessel” o “Córdoba”),
# temporada(“alta”, “baja”),
# cantidad de días que durará el viaje.
# importe del viaje
# altura del pasajero
# peso del pasajero
# sexo pasajero (F o M o NB)
# Viaja con equipaje de mano?
# paga con mercado , tarjeta o efectivo
# 1)
# a- cantidad de personas que viajan en cada temporada
# b- el peso acumulado de todos los que viajan a villa gesell
# c- el lugar con la mayor cantidad de días acumulados
# d- la suma de todos los importes

validar = 0
contador_dias = 0
contador_personas = 0
acumulador_peso = 0
cantidad_temporada = 0
suma_importes = 0
acumulador_dias_gessel = 0
acumulador_dias_cordoba = 0
acumulador_dias_madryn = 0
dias_max = 0



while validar == 0:
    validar = input("Desea ingresa estadias de vacaciones (si/no): ")
    if validar == "si":
        nombre = input("Ingrese su nombre: ")
        lugar = input("Ingrese su destino (“puerto madryn”, “villa gessel” o “cordoba”): ")
        temporada = input("Ingrese la temporada en la que quiere viajar (alta/baja): ")
        dias = int(input("Ingrese la cantidad de dias del viaje: "))
        importe = int(input("Ingrese el importe del viaje: "))
        altura = int(input("Ingrese su altura: "))
        peso = int(input("Ingrese su peso: "))
        sexo_pasajero = input("Ingrese su sexo (f/m/nb): ")
        equipaje = input("Viaja con equipaje de mano?(si/no): ")
        pago = input("Como desea pagar?(mercado/tarjeta/efectivo): ")
        
        while lugar != "villa gessel" and lugar != "puerto madryn" and lugar != "cordoba":
            lugar = input("Invalido! Ingrese su destino (“puerto madryn”, “villa gessel” o “cordoba”): ")
        
        while temporada != "alta" and temporada != "baja":
            temporada = input("Invalido! Ingrese la temporada en la que quiere viajar (alta/baja): ")
        
        while sexo_pasajero != "f" and sexo_pasajero != "m" and sexo_pasajero != "nb":
            sexo_pasajero = input("Invalido! Ingrese su sexo (f/m/nb): ")

        while equipaje != "si" and equipaje != "no":
            equipaje = input("Invalido! Viaja con equipaje de mano?(si/no): ")

        while pago != "mercado" and pago != "tarjeta" and pago != "efectivo":
            pago = input("Invalido! Como desea pagar?(mercado/tarjeta/efectivo): ")

        if temporada == "alta" or temporada == "baja":
            cantidad_temporada += 1

        if lugar == "villa gessel":
            acumulador_peso += peso
            acumulador_dias_gessel += 1
        elif lugar == "cordoba":
            acumulador_dias_cordoba += 1
        else:
            acumulador_dias_madryn += 1

        contador_dias += 1
        suma_importes += importe

        contador_personas += 1
    elif validar == "no":
        print("Fin del programa!!!")
        validar += 1

if acumulador_dias_gessel > acumulador_dias_cordoba and acumulador_dias_gessel > acumulador_dias_madryn:
    dias_max = acumulador_dias_gessel
elif acumulador_dias_cordoba > acumulador_dias_madryn:
    dias_max = acumulador_dias_cordoba
else:
    dias_max = acumulador_dias_madryn
        
print(f"La cantidad de personas que viajan en temporada es: {cantidad_temporada}")
print(f"El peso de los que viajan a villa gessel es: {acumulador_peso}")
print(f"La suma de los importes es: {suma_importes}")
print(f"El lugar con la mayor cantidad de dias es: {dias_max}")


