# 21 - Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, 
#calcule e mostre o valor da comissão e o salário final do funcionário.

funcionario = (input("Digite o nome do funcionario: "))

salario = float(input("Digite o salario de {}: ".format(funcionario)))

vendas = float(input("Digite qual foi o valor da venda mensal do funcionario {}: ".format(funcionario)))

comissao = (vendas * 4) / 100

sal_liquido = salario + comissao

print ("=" * 40 )

print ("O salario mensal de {} será de: R${}".format(funcionario, sal_liquido))

print ("=" * 40 )



