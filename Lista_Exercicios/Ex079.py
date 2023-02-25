# 79 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media = []

maior = []

igual = []

aluno_1 = []
m_a1 = []
aluno_2 = []
m_a2 = []
aluno_3 = []
m_a3 = []
aluno_4 = []
m_a4 = []
aluno_5 = []
m_a5 = []
aluno_6 = []
m_a6 = []
aluno_7 = []
m_a7 = []
aluno_8 = []
m_a8 = []
aluno_9 = []
m_a9 = []
aluno_10 = []
m_a10 = []

contador = 0

contador_1 = 0

contador_2 = 0

contador_3 = 0 

contador_4 = 0

contador_5 = 0

nome = input("Digite O nome do Primeiro Aluno: ")
aluno_1.append(nome)

while (contador < 4):

    nota = float(input("Digite a Nota do Aluno - 1 :"))

    contador += 1

    aluno_1.append(nota)

nome_1 = input("Digite O nome do Segundo Aluno: ")

aluno_2.append(nome_1)

while (contador_1 < 4):

    nota = float(input("Digite a Nota do Aluno - 2 :"))

    contador_1 += 1

    aluno_2.append(nota)

nome_2 = input("Digite O nome do Terceiro Aluno: ")
aluno_3.append(nome_2)

while (contador_2 < 4):

    nota = float(input("Digite a Nota do Aluno - 3 :"))

    contador_2 += 1

    aluno_3.append(nota)

nome_3 = input("Digite O nome do Quarto Aluno: ")
aluno_4.append(nome_3)

while (contador_3 < 4):

    nota = float(input("Digite a Nota do Aluno - 4 :"))

    contador_3 += 1

    aluno_4.append(nota)

nome_4 = input("Digite O nome do Quinto Aluno: ")
aluno_5.append(nome_4)

while (contador_4 < 4):

    nota = float(input("Digite a Nota do Aluno - 5 :"))

    contador_4 += 1

    aluno_5.append(nota)

print ("=" * 60)

print ("Alunos")

print ("=" * 60)

print ("Aluno 1")

print ("Nome: {}".format(aluno_1[0]))

print ("Notas: {}".format(aluno_1))

print ("Media De Notas: {}".format(m_a1))

print ("=" * 60)

print ("Aluno 2")

print ("Nome: {}".format(aluno_2[0]))

print ("Notas: {}".format(aluno_2))

print ("Media De Notas: {}".format(m_a2))

print ("=" * 60)

print ("Aluno 3")

print ("Nome: {}".format(aluno_3[0]))

print ("Notas: {}".format(aluno_3))

print ("Media De Notas: {}".format(m_a3))

print ("=" * 60)

print ("Aluno 4")

print ("Nome: {}".format(aluno_4[0]))

print ("Notas: {}".format(aluno_4))

print ("Media De Notas: {}".format(m_a4))







