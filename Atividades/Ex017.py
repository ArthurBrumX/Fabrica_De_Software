nome = input("Digite o nome do funcionario: ")

salario = float(input("Digite o Salario do funcionario {}: ".format(nome)))

if (salario == 280):
    reajuste = (salario * 20) / 100
    total = salario + reajuste
    print ("=" * 40)
    print ("O reajuste salarial do funcionario {}, será de R${}".format(nome, reajuste))
    print ("Após o reajuste o novo salario de {} será de: R${}".format(nome, total))
    print ("=" * 40)

elif (salario >= 281) or (salario <= 700):
    reajuste = (salario * 15) / 100
    total = salario + reajuste
    print ("=" * 40)
    print ("O reajuste salarial do funcionario {}, será de R${}".format(nome, reajuste))
    print ("Após o reajuste o novo salario de {} será de: R${}".format(nome, total))
    print ("=" * 40)

elif (salario >= 701) or (salario <= 1500):
    reajuste = (salario * 10) /  100
    total = salario + reajuste
    print ("=" * 40)
    print ("O reajuste salarial do funcionario {} será de R${}!".format(nome, reajuste))
    print ("Após o reajuste o novo salario de {} será de: R${}".format(nome, total))
    print ("=" * 40)

elif (salario > 1501):
    reajuste = (salario * 5) / 100
    total = salario + reajuste
    print ("=" * 40)
    print ("O reajuste salarial do funcinario {} será de R${} ".format(nome, reajuste))
    print ("Após o reajuste o novo salario de {} será de: R${}".format(nome, total))
    print ("=" * 40)