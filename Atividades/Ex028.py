turno = input("Em que turno voce estuda [M/V/N]: ")

if (turno == "M") or (turno == "m"):
    print ("Bom Dia!")

elif (turno == "V") or (turno == "v"):
    print ("Boa tarde!")

elif (turno == "N") or (turno == "n"):
    print("Boa noite!")

else:
    print("Valor invalido!")