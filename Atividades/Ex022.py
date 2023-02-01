produto = input("Digite o nome do produto: ")

valor = float(input("Digite o valor do produto R$ "))

desconto = valor * 10 / 100

novo_preco = valor - desconto

print ("O novo preco do produto {} será de: R${}".format(produto, novo_preco))