# 40 - João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. 
# Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um algoritmo que calcule e mostre quanto restará do salário do João

salario = 1200

conta_1 = 200

conta_2 = 120

val_juros_1 = conta_1 * 2 / 100

val_juros_2 = conta_2 * 2 /100

total_conta_1 = conta_1 + val_juros_1

total_conta_2 = conta_2 + val_juros_2

total_das_contas = total_conta_1 + total_conta_2

resto_salario = salario - total_conta_1 - total_conta_2

print ("O valor da primeira conta com juros é de: R$ {}".format(total_conta_1))

print ("O valor da segunda conta com jutos é de: R$ {}".format(total_conta_2))

print ("Ambas as contas juntas e com juros ficou no valor de: {}".format(total_das_contas))

print ("Após o pagamento das contas joao ficou com: R$ {}".format(resto_salario))