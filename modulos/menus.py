from modulos.importaciones import importar_listas
from modulos.validaciones import validar_ingreso_rango
from modulos.mostrar_datos import mostrar_lista
from modulos.mostrar_datos import mostrar_datos_filtrados
from modulos.mostrar_datos import ver_lista_unica
from modulos.modificaciones import agregar_lista
from modulos.inputs import pedir_dato
from modulos.mostrar_datos import ver_dato_exacto
from modulos.modificaciones import crear_lista_filtrada
from modulos.busquedas import comparar_datos
from modulos.modificaciones import ordenar_datos_descendente
from modulos.modificaciones import ordenar_lista_ascendente
from modulos.modificaciones import ordenar_lista_descendente
from modulos.modificaciones import eliminar_elemento




def generar_menu_opciones (op1:str, op2:str, op3:str, op4:str, op5:str, op6:str, op7:str, op8:str)->str:
    '''
    Brief: Genera el Menu General de opciones que el usuario le va pasando por parametro

    op1-op8: Strings pasados por parametro que seran las opciones del menu
    '''
    return f'''\n
    1-● {op1}                                  |   2-● {op2}
    3-● {op3}                                  |   4-● {op4}
    5-● {op5}|   6-● {op6}
    7-● {op7}                                          |   8-● {op8}
                                            9-● Salir
    '''

def generar_menu_opciones_simple(op1:str, op2:str)->str:
    '''
    Brief: Genera un menu de opciones simple (dos opciones) que el usuario le va psando por parametro

    op1 y op2: Strings pasados por parametro que seran las opciones del menu
    '''

    return f'''
    1-● {op1}
    2-● {op2}
    3-● Volver al menu principal
    '''

def generar_menu_opciones_regiones(op1:str, op2:str, op3:str, op4:str, op5:str, op6:str)->str:
    '''
    Brief: Genera un menu de 5 opciones que el usuario le va pasando por parametro

    op1-op4: Strings pasados por parametro que seran las opciones del menu
    '''


    return f'''
    1-● {op1}
    2-● {op2}
    3-● {op3}
    4-● {op4}
    5-● {op5}
    6-● {op6}
    7-● Volver al menu principal
    '''

def poke_menu ()->None:
    '''
    Brief: muestra el menu principal del programa y
        permite al usuario interactuar con la lista
        de pokemones mediante distintas opciones
    '''

    datos_importados = False
    bandera = True

    while bandera == True:
        print("\n ---- MENU PRINCIPAL ----")
        print(generar_menu_opciones("Importar la Lista de pokemones", "Ver Lista de pokemones", "Agregar un pokemon de la lista",
                                    "Eliminar un pokemon de la lista", "Ordenar la lista de pokemones alfabeticamente de la 'Z' a la 'A'",
                                    "Ver pokemon mas pesado de los tipo Agua", "Ver pokemon mas fuerte", "Ver pokemones de solo una region"))

        poke_opcion = validar_ingreso_rango(1, 9, "Ingrese una poke-opcion: ")

        if poke_opcion == 1:
            lista_pokemon = importar_listas()
            datos_importados = True
            print("\n--- DATOS IMPORTADOS CORRECTAMENTE ---")

        elif poke_opcion != 0 and datos_importados == False:
            print("\n--- Primero debe importar la poke-lista (opción 1) ---")

        elif poke_opcion == 2:
            print("\n --- VER POKE-LISTA --- ")
            mostrar_lista(lista_pokemon)

        elif poke_opcion == 3:
            print("\n --- AGREGAR UN POKEMON --- ")
            agregar_lista(lista_pokemon, "Ingresar", "del pokemon")

        elif poke_opcion == 4:
            print("\n --- ELIMINAR UN POKEMON --- ")
            poke_eliminado = pedir_dato(lista_pokemon, 0, "Ingrese el nombre el Pokemon a eliminar: ")
            
            ver_dato_exacto(lista_pokemon, poke_eliminado, 0, "\n --- POKEMON ELIMINADO: ")

            ver_lista_unica(lista_pokemon, poke_eliminado)

            eliminar_elemento(lista_pokemon, poke_eliminado)
        elif poke_opcion == 5:
            print("\n --- ORDENAR LISTA --- ")
            print(generar_menu_opciones_simple("Ordenar la lista de la 'A' a la 'Z'", "Ordenar la lista de la 'Z' a la 'A'"))

            opcion_ordenamiento = validar_ingreso_rango(1,3, "Ingrese una opcion para ordenar la lista: ")
            
            if opcion_ordenamiento == 1:
                print("\n --- ORDENASTE LA LISTA ASCENDENTEMENTE --- ")
                ordenar_lista_ascendente(lista_pokemon)
            elif opcion_ordenamiento == 2:
                print("\n --- ORDENASTE LA LISTA DESCENDENTEMENTE --- ")
                ordenar_lista_descendente(lista_pokemon)
            else:
                print("Volviendo al menu principal")
        elif poke_opcion == 6:
            print("\n --- POKEMON MAS PESADO TIPO AGUA --- ")
            lista_agua = crear_lista_filtrada(lista_pokemon, "Agua", 1)
            ordenar_datos_descendente(lista_agua, 3)
            ver_lista_unica(lista_agua, 0)
        elif poke_opcion == 7:
            print("\n --- POKEMON/ES MAS FUERTES --- ")
            mas_fuerte = comparar_datos(lista_pokemon, 0, 5)

            print("Pokemon/es con mayor fuerza de ataque: ")

            mostrar_datos_filtrados(lista_pokemon, mas_fuerte, 5)
            
        elif poke_opcion == 8:
            print("\n  ---REGIONES--- ")
            print(generar_menu_opciones_regiones("La region Kanto", "La region Sinnoh", "La region Kalos", "La region Hoenn", "La region Johto", "La region Unova"))

            opcion_region = validar_ingreso_rango(1, 7, "Ingrese una region para ver a los pokemones de dicha region: ")

            if opcion_region == 1:
                print("\n --- POKEMONES DE KANTO --- ")
                lista_kanto = crear_lista_filtrada(lista_pokemon, "Kanto", 6)
                mostrar_lista(lista_kanto)
            elif opcion_region == 2:
                print("\n --- POKEMONES DE SINNOH --- ")
                lista_sinnoh = crear_lista_filtrada(lista_pokemon, "Sinnoh", 6)
                mostrar_lista(lista_sinnoh)
            elif opcion_region == 3:
                print("\n --- POKEMONES DE KALOS --- ")
                lista_kalos = crear_lista_filtrada(lista_pokemon, "Kalos", 6)
                mostrar_lista(lista_kalos)
            elif opcion_region == 4:
                print("\n --- POKEMONES DE HOENN --- ")
                lista_hoenn = crear_lista_filtrada(lista_pokemon, "Hoenn", 6)
                mostrar_lista(lista_hoenn)
            elif opcion_region == 5:
                print("\n --- POKEMONES DE JOHTO --- ")
                lista_Johto = crear_lista_filtrada(lista_pokemon, "Johto", 6)
                mostrar_lista(lista_Johto)
            elif opcion_region == 6:
                print("\n --- POKEMONES DE UNOVA --- ")
                lista_Unova = crear_lista_filtrada(lista_pokemon, "Unova", 6)
                mostrar_lista(lista_Unova)
            else:
                print("Volviendo al menu principal")
                
        else:
            print("Saliste del Poke-Menu!!!")
            bandera = False
