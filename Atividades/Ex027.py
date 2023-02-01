sexo = input("Qual o sexo da pessoa [M/F]: ")
altura = float(input("Qual sua altura: "))

if (sexo == "M") or (sexo =="m") or (sexo == "Masculino") or (sexo == "masculino"):
    imc = (72.7 * altura) - 58
    print ("Seu peso ideal é de {} kg!".format(imc))

elif (sexo == "F") or (sexo =="f") or (sexo == "Feminino") or (sexo == "Feminino"):
    imc = (62.1 * altura) - 44.7
    print ("Seu peso ideal é de {} kg!".format(imc))
