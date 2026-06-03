edad = input("ingrese edad: ")
edad = int(edad)

if edad >= 18:
    print("regristrado ok")
elif edad > 12:
    print("hace el test")
    test = input("test (si o no)")
    if test == "si":
        print("regristrado ok")
    else:
        print("no quisiste el test")
else:
    print("sos menor")

v1 = "outfit"
v2 = "outfit"

condicion = v1 == v2
if condicion:
    pass

True == False

match v1:
    case "bla":
        print("no matchea")
    case "si":
        print("matcheamos")
    case _:
        print("else")

