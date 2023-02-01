nome = input ("Qual é o seu nome: ")
diciplina = input("Qual diciplina vc estuda: ")
nota_1 = float(input("Qual é a primeira nota da prova: "))
nota_2 = float (input("Qual é a segunda nota da prova: "))
nota_3 = float (input("Qual é a terceira nota da prova: "))

media = (nota_1 + nota_2 + nota_3) / 3

print ("=" * 40)

print ("O aluno {}, que esta cursando a diciplina de: {} tirou: \nNa primeira prova: {} \nNa segunda nota: {} \nNa terceira nota: {} \nSua nota final será: {}".format(nome, diciplina, nota_1, nota_2, nota_3, media))

print ("=" * 40)