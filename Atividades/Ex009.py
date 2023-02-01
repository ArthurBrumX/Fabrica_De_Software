nome = input("Qual o nome do aluno: ")
diciplina = input("Referente a qual diciplina voce deseja aplicar as notas: ")

nota_1 = float(input("Qual a nota da primeira prova: "))
nota_2 = float(input("Qual a nota da segunda prova: "))
nota_3 = float(input("Qual a nota da terceira prova: "))

media = (nota_1 + nota_2 + nota_3) / 3

if (media >= 6.0):
    print ("A media do aluno {} é {:.1f} ALUNO APROVADO!".format(nome, media))

elif ():
    print("a media do aluno {} é {:.1f} ALUNO REPROVADO!".format(nome, media))