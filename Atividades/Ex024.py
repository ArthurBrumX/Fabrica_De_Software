pergunta = int(input("Qual a quantidade de sanduiches que voce deseja: "))

grama_pre = 50
grama_quei = 50
grama_hamb = 100

conta = pergunta * grama_pre

conta_1 = pergunta * grama_quei

conta_2 = pergunta * grama_hamb

sanduiche = grama_pre + grama_quei + grama_hamb

peso = pergunta * sanduiche

print ("Para fazer {} sanduiches:".format(pergunta))

print ("voce precisa-rá de {} gramas de queijo!".format(conta_1))

print ("Voce precisa-rá de {} gramas de presunto!".format(conta))

print ("Voce precisa-rá de {} gramas de hamburger!".format(conta_2))

if (peso <= 999):
    print ("No total os seus sanduiches vão pesar {} gramas".format(peso))

elif(peso >999):
    print("No total os seus sanduiches vão pesar kg {}".format(peso))



