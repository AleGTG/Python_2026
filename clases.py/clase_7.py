#Vamos a importar modulos a archivos
#el objetivo es utilizar la funcion del modulo_c_7 en este codigo

#manera numero 1
import modulo_calculos
import modulo_mensajes

modulo_mensajes.mostrar_datos_persona()#una manera de invocar una funcion de otro modulo

#segunda manera
from modulo_calculos import * # importa todo el modulo
from modulo_calculos import sumar # importa cosas especificas

retorno = sumar(1, 2)
print(retorno)

###############################################################
#   PAQUETESSSSS
#       LOS MODULOS SE DIVIDEN SEGUN SU FUNCIONALIDAD
#   UN PAQUETE SE INICIA CON "__init__.py"
#   una aplacion es un paquete y a la vez no
