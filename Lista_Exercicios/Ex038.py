# 38 - O restaurante a quilo Sabor em Quilo cobra R$59,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) 
# e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

peso_prato = float(input("KG do prato: "))

peso_KG = 59

valor_total_prato = peso_prato * peso_KG

print ("O valor a ser pago pelo prato feito é de: R$ {}".format(valor_total_prato))
