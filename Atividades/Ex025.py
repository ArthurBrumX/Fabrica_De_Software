c_pequenas = float(input("Quantas camisas pequenas vai querer: "))

c_medias = float(input("Quantas camisas medias vai querer: "))

c_grandes = float(input("Quantas camisas grandes vai querer: "))

p = 10

m = 12

g = 15

total_p = c_pequenas * p

total_m = c_medias * m

total_g = c_grandes * g

total_compra = total_p + total_m + total_g

print ("A sua compra foi no total de R${} reais!".format(total_compra))