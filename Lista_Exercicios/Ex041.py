# 41 - Três amigos, Joceyr, Thiago e Alexandre. decidiram rachar igualmente a conta de um bar. 
# Faça um algoritmopara ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que Joceyr e Thiago não paguem centavos. 
# Ex: uma conta de R$101,53 resulta em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53 para Alexandre.


valor_conta = float(input("Digite o valor total da conta: "))

divisao = valor_conta / 3

print (divisao)

joceyr = round(divisao)

alexandre = round(divisao)

thiago = valor_conta -joceyr- alexandre

print ("O valor que Joceyr irá pagar é de: R$ {}".format(joceyr))
print ("O valor que Alexandre irá pagar é de: R$ {}".format(alexandre))
print (f"O valor que thiago irá {thiago}pagar é de: R$ {thiago:.2f}")

