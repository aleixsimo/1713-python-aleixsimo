hi_ha_negatiu = False

for i in range(10):
    numero = float(input("Introdueix un número: "))
    if numero < 0:
        hi_ha_negatiu = True

if hi_ha_negatiu:
    print("Hi ha almenys un número negatiu.")
else:
    print("No hi ha cap número negatiu.")
