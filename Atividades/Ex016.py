resposta = "S"
soma = quant = media = maior = menor = 0
while resposta in "Ss":
    num = int(input("Digite um numero "))

    soma += num
    quant += 1

    if quant == 1:
        maior = menor

    else:
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num


    resposta = input("Quer continuar? [S / N]: ").upper() .strip()[0]

media = soma / quant

print ("Voçe digitou {} numero e a media foi {}".format(quant, media))
print ("O maior valor digitado foi {} e o menor valor digitado é {}". format(maior, menor))