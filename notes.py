def buscar_min(lista:list, indice:int)->list:
    minimo = []
    if len(lista) > 0:

        minimo = lista[0]
        for i in range(len(lista)):
            if lista[i][indice] < minimo[indice]:
                minimo = lista [i]
    
    return minimo
    

a = [
    [
        1,2,3,4,5,4
    ],
    [
        1,2,55,6,777,8
    ],
]
b=[]

prueba = buscar_min(b,0)

print(prueba)