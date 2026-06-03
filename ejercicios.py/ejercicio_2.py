'''La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes para preparar comida al por mayor. En total, sabemos que se realizarán 10 compras de ingredientes.

Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).

Además, tener en cuenta que si compro más de 100 kilos en total tengo un 15% de descuento sobre el precio bruto, o si compro más de 300 kilos en total, 
tengo un 25% de descuento sobre el precio bruto.

Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
E. Porcentaje de variedad animal sobre el total'''

contador_compras = 0
acumulador_kilo = 0

acumulador_precio = 0

total_bruto = 0

contador_animal = 0

while contador_compras < 2:
    peso = int(input("Ingrese el peso que quiera comprar (entre 10 y 100 kg): "))
    precio = int(input("Ingrese el precio por kilo (mayor a 0): ")) # 1kg = 100$
    variedad = input("Ingrese el tipo de compra (vegetal, animal, mezcla): ")
    #print(contador_compras)
    if peso >= 10 or peso <= 100 and precio > 0 and (variedad == "animal" or variedad == "vegetal" or variedad == "mezcla"):
        #el primer if sirve pero no esta del todo bien

        importe = peso * precio
        total_bruto += importe
        acumulador_kilo += peso
        acumulador_precio += precio

    if variedad == "animal":
        contador_animal = contador_animal + 1
        #los if se podria hacer con un match
    if contador_compras == 0 or precio > precio_maximo:
        precio_maximo = precio
        variedad_cara = variedad

    else:
        print("ERROR") #datos mal ingresados o no ingresados
    
    contador_compras = contador_compras + 1

if acumulador_kilo > 300:
    descuento = total_bruto * 0.25 # 25 / 100
elif acumulador_kilo > 100:
    descuento = total_bruto * 0.15 # 25 / 100
else:
    descuento = 0

total_con_descuento = total_bruto - descuento

promedio_precio = acumulador_precio / contador_compras

pocentaje_animal = (contador_animal * 100) / contador_compras

print(f"Total bruto es: {total_bruto}")
print(f"Total con descuento es: {total_con_descuento}")
print(f"Tipo mas caro es: {variedad_cara}")
print(f"Promedio precio por kilo es: {promedio_precio}")
print(f"El porcentaje animal es: {pocentaje_animal}%")

