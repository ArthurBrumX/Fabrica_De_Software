lado_1 = float(input("Digite o primeiro lado do triangulo: "))

lado_2 = float(input("Digite o segunfo lado do triangulo: "))

lado_3 = float(input("Digite o terceiro lado do triangulo: "))

if (lado_1 == lado_2) and (lado_2 == lado_3):
    print("É um triangulo Equilátero!")
        # Um triangulo equilátero é formado por tres lados iguais.

elif (lado_1 == lado_2) and (lado_2 == lado_1) and (lado_3 != lado_1 and lado_2):
    print("É um triangulo Isósceles!")
        # Um triangulo Isósceles é formado por apenas 2 lados iguais e o terceiro lado diferente.

elif (lado_1 != lado_2) and (lado_2 != lado_3):
    print("É um triangulo Escaleno!")
        # Um triangulo Escaleno é formado por todos os lados deferente um do outro.