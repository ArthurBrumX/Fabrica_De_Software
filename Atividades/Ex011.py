nome = input("Qual é o seu nome: ")
idade = int(input("Qual é sua idade: "))

if (idade <= 2):
    print ("{} está com {} e pela tabela é considerado um bebê! ".format(nome, idade))

elif (idade >= 3) or (idade <= 11):
    print ("{} esta com {} e pela tabela é considerado uma criança! ".format(nome, idade))

elif (idade >= 12) or (idade <= 21):
    print ("{} esta com {} e pela tabela é considerado um jovem! ".format(nome, idade))

elif (idade >= 22) or (idade <= 64):
    print ("{} esta com {} e pela tabela é considerado um adulto! ".format(nome, idade))

elif (idade >= 65) or (idade <= 100):
    print ("{} esta com {} e pela tabela é considerado um ! ".format(nome, idade))

elif (idade >= 101):
    print ("{} esta com {} e pela tabela é considerado uma pessoa muito velhinha") 