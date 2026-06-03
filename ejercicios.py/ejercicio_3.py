'''para ingresar a una app tengo que escribir de la mismima la 
contraseña es "UTN350 o UTN100"

cuando entre le muestro un mesajito que diga bienvenido a la UTN'''

contraseña = str(input("Ingrese la contraseña: "))

while contraseña != "UTN350" and contraseña != "UTN100":
    contraseña = str(input("ERROR! Ingrese la contraseña: "))

print("bienvenido a la UTN")