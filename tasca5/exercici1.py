# Calcular el preu total d'un producte sumant el preu del producte i el preu de la mà d'obra.

def calcular_preu(preu_producte, preu_maobra):
    preu_total = preu_producte + preu_maobra
    return preu_total

resultat = calcular_preu(35, 40)
print(f"El preu total és: {resultat}")

# Funció per aplicar un descompte segons el client.

def aplicar_descompte(preu, tipus_client):
    if tipus_client == "Client_Habitual":
        descompte = preu * 0.15  # 15% de descompte per clients habituals
    elif tipus_client == "Empresa":
        descompte = preu * 0.1  # 10% de descompte per empreses
    elif tipus_client == "Particular":
        descompte = 0  # Cap descompte per a particulars
    else:
        # Si el tipus de client no és reconegut, s'aplica error
        print ("Error: Tipus de client no reconegut. No s'aplica cap descompte.")
        descompte = 0  # No s'aplica cap descompte per a clients desconeguts

    preu_final = preu - descompte
    return preu_final

resultat = aplicar_descompte(75, "Client_Habitual")
print(f"El preu final amb descompte és: {resultat}")
resultat = aplicar_descompte(75, "Empresa")
print(f"El preu final amb descompte és: {resultat}")
resultat = aplicar_descompte(75, "Particular")
print(f"El preu final amb descompte és: {resultat}")
resultat = aplicar_descompte(75, "Altre")  # Exemple de client desconegut
print(f"El preu final amb descompte és: {resultat}")

# Funcions que criden altres funcions

def aplicar_descompte(preu, tipus_client):

    if tipus_client == "Particular":
        return preu
    elif tipus_client == "Empresa":
        return preu * 0.90
    elif tipus_client == "Client_Habitual":
        return preu * 0.85
    else:
        print("Error: El tipus de client no és vàlid.")
        return preu

def calcular_iva(preu):
    return preu * 0.21

def calcular_factura(preu, tipus_client):
    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)
    return preu_descompte + iva

print(calcular_factura(100, "Particular"))
print(calcular_factura(100, "Empresa"))
print(calcular_factura(100, "Client_Habitual"))
print(calcular_factura(100, "Altre"))