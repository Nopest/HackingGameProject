# TODO  Faire une ouverture de fichier xml  ou une extraction de donnée via XPATH
# et verifier que l'adresse tirée est differente qu'une pré-existante
def randIp():
    import random
    return str(random.randint(1,254))+'.'+str(random.randint(1,254))+'.'+str(random.randint(1,254))+'.'+str(random.randint(1,254))

print(randIp())