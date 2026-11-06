hi_ha_algun_10 = False

nota = float(input("Introdueix una nota (de 0 a 10, o -1 per acabar): "))
while nota != -1:
    if nota == 10:
        hi_ha_algun_10 = True
    nota = float(input("Introdueix una nota (de 0 a 10, o -1 per acabar): "))

if hi_ha_algun_10:
    print("Hi ha almenys una nota de 10.")
else:
    print("No hi ha cap nota de 10.")

