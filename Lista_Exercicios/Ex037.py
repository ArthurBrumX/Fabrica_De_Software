# 37 - A padaria Super Pão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pãozinho custa R$ 1,00 e a broa custa R$ 3,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar 
# numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades 
# de pães e de broas, e depois calcular os dados solicitados.

paozinho = 1
broa = 3.50

venda_1 = float(input("Qual a Quantidade de Pães vendidos No Dia: R$ "))

venda_2 = float(input("Qual a Quantidade de Broas vendidos No Dia: R$ "))

total_venda = venda_1 + venda_2

poupanca = total_venda * 10 / 100

print ("O total da venda do dia é: R${}".format(total_venda))

print ("O 10% que será guardado na poupança será de: R${}".format(poupanca))