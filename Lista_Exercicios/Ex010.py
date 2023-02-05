# 10 - Faça um algoritmo que verifique se o número digitado é menor, maior ou igual a 10 e apresente a mensagem referente ao número.

numero = float(input("Digite Um Numero: "))

if (numero < 10):
    print ("Voce digitou {}".format(numero))
    print ("O numero digitado é menor que 10!")

elif (numero > 10):
    print ("Voce digitou {}".format(numero))
    print ("O numero digitado é maior que 10!")

elif (numero == 10):
    print ("Voce digitou {}".format(numero))
    print ("O numero digitado é igual a 10!")