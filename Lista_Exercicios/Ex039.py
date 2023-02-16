# 39 - Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. 
# Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.

dia = int(input("Digite o dia atual: "))
mes = int(input("Digite o mes atual: "))

dia_atual = 365 - dia
mes_atual = 12 - mes

print (dia_atual)
print (mes_atual)

