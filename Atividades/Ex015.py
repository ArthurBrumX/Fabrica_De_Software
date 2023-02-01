sexo = input("Digite o seu sexo: ")

if (sexo == "masculino") or (sexo == "Masculino"):
    identificador = "M"
    print ("Voce é do sexo {}".format(identificador))

elif (sexo == "feminino") or (sexo == "Feminino"):
    identificador = "F"
    print ("Voce é do sexo {}".format(identificador))

elif (sexo != "masculino") or (sexo != "Masculino") or (sexo != "feminino") or (sexo != "Feminino"):
    print ("Sexo Invalido!")