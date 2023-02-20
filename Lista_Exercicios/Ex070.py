# 70 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior
# resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as
# cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o
# melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da
# execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto: 6.5 m
# Pior salto: 5.3 m

contador = 0

melhor_salto = 0

pior_salto = 0 

cont_salto = 0

primeiro = 0

segundo = 0

terceiro = 0

quarto = 0

quinto = 0

nome = input("- Informe o Nome Do Atleta: ")

while (cont_salto < 5):

    cont_salto = cont_salto + 1

    salto = float(input("- Informe a Distancia Do Salto: "))

    contador = contador + 1

    if (contador == 1):

        melhor_salto = salto

        pior_salto = salto

    else:

        if (salto > melhor_salto):

            melhor_salto = salto
        
        if (salto < pior_salto):

            pior_salto = salto

media = segundo + terceiro + quarto / 5

print ("- Melhor Salto: {}".format(melhor_salto))

print ("- Pior Salto: {}".format(pior_salto))

print (salto)

print (media)

print (contador)





















































"""nome = input("- Informe o Nome Do Atleta: ")

primeiro = float(input("- Informe a Distancia Do Primeiro Salto: "))
segundo = float(input("- Informe a Distancia Do Segundo Salto: "))
terceiro = float(input("- Informe a Distancia Do Terceiro Salto: "))
quarto = float(input("- Informe a Distancia Do Quarto Salto: "))
quinto = float(input("- Informe a Distancia Do Quinto Salto: "))

media = segundo + terceiro + quarto / 5"""







