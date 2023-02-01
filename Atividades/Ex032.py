nome = input("Qual é o seu nome: ")
sexo = input("Qual é o seu sexo: [M/F]: ")
estado_civil = input("Qual seu estado civil: ")

if (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):
    if (estado_civil == "Casada") or (estado_civil == "casada"):

        tempo = int(input("Quanto tempo de casada voce tem: "))
        print("voce se chama {}, é do sexo {} e tem {} anos de casada!".format(nome, sexo, tempo))

    else:
        print("voce se chama {} e é do sexo {}".format(nome, sexo))

elif (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):
    print("voce se chama {} e é do sexo {}!".format(nome,sexo))