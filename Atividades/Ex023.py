n_galinhas = int(input("granja TecFrango - Digite o numero de galinhas presentes no galinheiro: "))

p_direito = 4.00

p_esquerdo = 2 * 3.50

galinha = p_direito + p_esquerdo

total = n_galinhas * galinha

print ("O total gasto no galinheiro será de: R${}".format(total))
