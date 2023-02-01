funcionario = (input("Digite o nome do funcionario: "))

salario = float(input("Digite o salario de {}: ".format(funcionario)))

vendas = float(input("Digite qual foi o valor da venda mensal do funcionario {}: ".format(funcionario)))

comissao = (vendas * 4) / 100

sal_liquido = salario + comissao

print ("=" * 40 )

print ("O salario mensal de {} será de: R${}".format(funcionario, sal_liquido))

print ("=" * 40 )
