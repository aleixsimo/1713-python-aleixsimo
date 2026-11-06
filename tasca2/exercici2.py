# Calculadora 2
numero1 = int(input("Introdueix el primer número: "))
numero2 = int(input("Introdueix el segon número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacio = numero1 * numero2

print(f"suma: {numero1} + {numero2} = {suma}")
print(f"resta: {numero1} - {numero2} = {resta}")
print(f"multiplicació: {numero1} * {numero2} = {multiplicacio}")

if numero2 != 0:
    divisio = numero1 / numero2
    print(f"divisió: {numero1} / {numero2} = {divisio}")

else:
    print(f"No es pot dividir per zero.")
