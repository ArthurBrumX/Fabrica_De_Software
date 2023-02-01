valor_produto = float(input("Qual o valor do produto: "))

if (valor_produto >= 50):
    reajuste = (valor_produto * 45) / 100
    total = valor_produto + reajuste
    print ("O valor do produto passa-ra a ser de R${} reais".format(total))

elif (valor_produto < 50):
    reajuste = (valor_produto * 30) / 100
    print ("O lucro desta venda foi de R${} reais".format(reajuste))
