# Consigna 2
# Una fábrica textil registra la producción de lotes de tela en un día de trabajo. No hay un total
# de registros mínimo ni se sabe cuántos habrá en total.
# Por cada lote se ingresan:
# ● Tipo de tela (algodón, poliéster, mezcla)
# ● Cantidad producida en metros (entre 100 y 5000)
# ● Costo por metro (mayor a 0)
# ● Calidad (primera, generica)
# Todos los datos deben ser validados.
# Consideraciones:
# ● Los productos de calidad premium tienen un descuento del 10% sobre su precio
# bruto
# ● Si el costo por metro promedio de los lotes es mayor a 50, se aplica un impuesto
# adicional del 10% sobre el total bruto.
# ● Si la producción total supera los 30000 metros, se aplica un recargo del 10% en
# concepto de impuestos.
# Se pide:
# a. Calcular el costo total bruto de producción. Luego, calcular el costo total final con
# descuentos e impuestos (informar qué descuento y/o qué recargo se le aplica al precio).
# b. Cuál fue el costo por metro del lote de algodón más corto en cantidad producida
# (metros).
# c. ¿Qué porcentaje de los lotes fue de mezcla?.
# d. Se produjeron más lotes de primera o de genérica?
# e. Informar cuántos lotes son de calidad primera.

impuesto = 0.10
cont_registro = 0
total_bruto = 0
cont_metros = 0
cont_lotes = 0
cont_tipo_tela = 0
cont_mezcla = 0
cont_generica = 0
cont_primera = 0
contador_algodon = 0
contador_poliester = 0


while cont_registro == 0:
    resgistro = input("Desea registrar un lote de produccion? (si/no): ")
    if resgistro == "si":

        metros = int(input("Ingrese la cantidad de metros (entre 100 y 5000)): "))
        while metros <= 100 and metros >= 5000:
            metros = int(input("valor invalido ingrese los metros devuelta: "))

        tela = str(input("Ingrese el tipo de tela (algodon/poliester/mezcla): "))
        while tela != "algodon" and tela != "poliester" and tela != "mezcla":
            tela = str(input("valor invalido ingrese el tipo de tela devuelta: "))

        costo = int(input("Ingrese el costo por metro (mayor a 0): "))
        while costo <= 0:
            costo = int(input("Costo invalido ingrese el costo devuelta: "))

        calidad = str(input("Ingrese la calidad de la tela (primera/generica): "))
        while calidad != "primera" and calidad != "generica":
            calidad = str(input("Tipo de calidad invalida ingrese la calidad devuelta: "))

        if tela == "mezcla":
            cont_mezcla += 1
        elif tela == "algodon":
            contador_algodon == 0

        
        

        if calidad > "primera":
            cont_primera += 1
        else:
            cont_generica += 1



        importe = metros * costo
        total_bruto += importe
        descuento_premium = total_bruto * impuesto
        cont_lotes += 1

    elif resgistro == "no":
        print("Registro terminado!!!")
        cont_registro = cont_registro + 1

porcentaje_mezcla = (cont_mezcla * 100) / cont_lotes