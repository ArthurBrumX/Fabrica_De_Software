destino = input("Qual será o destino: ")
tempo = float(input("Quanto tempo de viajem: "))
distancia = float(input("Quantos km seu veiculo roda por km: "))

gasolina = 5.4

km = distancia * gasolina

custo = tempo * km


print ("Para chegar até {}, voce irá gastar R${} de gasolina, isso supondo que nao acontecerá nenhum imprevisto.".format(destino, custo))
