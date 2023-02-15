# 36 - O cardápio da lanchonete Burgão é o seguinte:

# ESPECIFICAÇÃO CÓDIGO PREÇO

# Cachorro Quente       100         R$ 11,20
# Ovo Simples           101         R$ 8,30
# Bauru com Ovo         102         R$ 11,50
# Hambúrguer            103         R$ 16,20
# Refrigerante          201         R$ 6,00
# Suco                  202         R$ 7,50
# Água Mineral          203         R$ 4,70

# Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente.

# Assumaas entradas corretas:

cachorro_quente = 11.20
ovo_simples = 8.30
bauru_com_ovo = 11.50
hamburguer = 16.20
refrigerante = 6.0
suco = 7.50
agua_mineral = 4.70
carrinho = 0

print ("Cachorro Quente --> Código Do Produto: [100]")
print ("Ovo Simples     --> Código Do Produto: [101]")
print ("Bauru Com Ovo   --> Código Do Produto: [102]")
print ("Hamburger       --> Código Do Produto: [103]")
print ("Refrigerante    --> Código Do Produto: [201]")
print ("Suco            --> Código Do Produto: [202]")
print ("Agua Mineral    --> Código Do Produto: [203]")

resposta = input("Deseja fazer o Pedido [S/N]: ")

while (resposta == "Sim") or (resposta == "sim"):    

    
    codigo = input("Digite o código do produto: ")

    if (codigo == "100"):

        carrinho = carrinho + cachorro_quente
        print ("+ 1 cachorro quente")

    if (codigo == "101"):

        carrinho = carrinho + ovo_simples
        print ("+ 1 Ovo Simples")

    if (codigo == "102"):

        carrinho = carrinho + bauru_com_ovo
        print ("+ 1 Bauru Com Ovo")

    if (codigo == "103"):

        carrinho = carrinho + hamburguer
        print ("+ 1 Hamburger")

    if (codigo == "201"):

        carrinho = carrinho + refrigerante
        print ("+ 1 Refrigerante")

    if (codigo == "202"):

        carrinho = carrinho + suco
        print ("+ 1 Suco")

    if (codigo == "203"):

        carrinho = carrinho + agua_mineral
        print ("+ 1 Agua Mineral")

    resposta = input("Deseja continuar o Pedido [S/N]: ")
