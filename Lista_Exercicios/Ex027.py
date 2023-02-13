# 27 - O departamento de Educação Física deseja informatizar este setor e colocou à disposição os seguintes dados de 50 alunos:

# Matrícula, sexo (M, F), altura (cm) e status físico (1–bom, 2–regular, 3–ruim)

# Estes dados deverão ser lidos através de uma unidade de entrada qualquer.

# Calcular e imprimir:

# a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.

# b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo masculino) cujo status físico seja bom.


aluno = 0

total_de_mulheres = 0

total_de_mulheres_altas = 0

total_de_homens = 0

# ================================

bons = 0

porcentagem =0

# ================================


while aluno < 2:

    sexo = input("Digite seu sexo: ")
    altura = float(input("Digite a altura: "))
    status = int(input("Digite o status: "))

    if (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):

        if (altura >= 1.70):

            total_de_mulheres = total_de_mulheres + 1
            total_de_mulheres_altas = total_de_mulheres_altas + 1

        elif (altura < 1.70):
            
            total_de_mulheres = total_de_mulheres + 1

    elif (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):

        if (status == 1):

            bons = bons + 1

            porcentagem = total_de_homens * 50 / 100

            total_de_homens = total_de_homens + 1

        elif (status != 1 ):

            total_de_homens = total_de_homens + 1

    aluno = aluno + 1

print ("Total de mulheres altas: {}".format(total_de_mulheres_altas))

print ("Total de homens {}".format(porcentagem))