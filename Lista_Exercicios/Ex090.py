# 90 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas 
# vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

# • $200 - $299
# • $300 - $399
# • $400 - $499
# • $500 - $599
# • $600 - $699
# • $700 - $799
# • $800 - $899
# • $900 - $999
# • $1000 em diante

# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

faixas_salarios = [[200,299],[300,399],[400,499],[500,599],[600,699], [700,799],[800,899],[900,999]]
quantidades = [0,0,0,0,0,0,0,0,0]

salarios = []
valor_vendas = True
while valor_vendas != 0:
    valor_vendas = float(input("\nDigite a valor das vendas: $ "))
    if valor_vendas == 0:
        break
    else:
        salario = (valor_vendas * 0.09) + 200
        print(f'R$ {salario:.2f}')
        if salario < 1000:
            for i in range(len(faixas_salarios)):
                if salario >= faixas_salarios[i][0] and salario < faixas_salarios[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
print('\n' * 3)
for i in range(len(faixas_salarios)):
    print('Faixas de Salários:')
    print(f'Entre $ {faixas_salarios[i][0]:.2f} e R$ {faixas_salarios[i][1]:.2f}: {quantidades[i]}')
print(f'Salarios maiores que $1000: {quantidades[8]}')