numero = float(input("Digite o numero da sua conta: "))

saldo = float(input("Digite seu saldo bancario: "))

debito = float(input("Digite seu debito bancario: "))

credito = float(input("Digite seu credito bancario: "))

saldo_atual = saldo - debito + credito

if (saldo_atual >= 0):
    print ("O seu saldo é de R${}!".format(saldo_atual))
    print ("o seu saldo bancario esta positivo!")

elif (saldo_atual <= -1):
    print ("O seu saldo é de R${}!!".format(saldo_atual))
    print ("O seu saldo esta negativo!!!")
    