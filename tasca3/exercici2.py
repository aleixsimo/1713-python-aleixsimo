nombre1 = input("Introdueix el primer nombre: ")
nombre2 = input("Introdueix el segon nombre: ")
nombre3 = input("Introdueix el tercer nombre: ")

if nombre1.isdigit() and nombre2.isdigit() and nombre3.isdigit():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
    nombre3 = int(nombre3)

    if nombre1 > nombre2 and nombre1 > nombre3:
        print(f"El nombre més gran és: {nombre1}")
    elif nombre2 > nombre1 and nombre2 > nombre3:
        print(f"El nombre més gran és: {nombre2}")
    else:
        print(f"El nombre més gran és: {nombre3}")
