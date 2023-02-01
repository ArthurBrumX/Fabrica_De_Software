# folha de pagamento

nome = input("Digite seu nome: ")

hora_trab = float(input("Quanta horas por mes voce trabalha: "))

valor_hora_trab = float(input("Qual o valor da sua hora trabalhada: "))

salario_bruto = valor_hora_trab * hora_trab

sindicato = (salario_bruto * 3) / 100

FGTS = (salario_bruto * 11) / 100

# salario_liquido = salario_bruto - sindicato - FGTS

if (salario_bruto <= 900):
    print("Voce esta isento!")

elif (salario_bruto > 900) or (salario_bruto <= 1500):
    descont_IR = salario_bruto * 5 / 100
    salario_liquido = salario_bruto - sindicato - descont_IR - FGTS
    print ("Seu salario liquido sera de R${}".format(salario_liquido))

elif (salario_bruto > 1500) or (salario_bruto <= 2500):
    descont_IR = salario_bruto * 10 / 100
    salario_liquido = salario_bruto - sindicato - descont_IR - FGTS
    print ("Seu salario liquido sera de R${}".format(salario_liquido))

elif (salario_bruto > 2500):
    desconto_IR = salario_bruto * 20 /100
    salario_liquido = salario_bruto - sindicato - desconto_IR - FGTS
    print ("Seu salario liquido sera de R${}".format(salario_liquido))    


