n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
op = input("Qual operacao matematica voce deseja realizar: ")

if (op == "Adição") or (op == "Adicao") or (op == "Adição") or (op == "adicao"):
    soma = n1 + n2
    p_i = soma % 2

    if(p_i == 0):
        print("A soma dos numero é par! ")

    elif(p_i == 1):
        print("A soma dos numero é impar!")
    
    if(soma >= 0): 
        print("A soma dos numero é positivo!")

    elif(soma <= -1):
        print("A soma dos numero é negativo!")

    if (soma == int):
        print("A soma dos numero é inteiro!")
    
    elif (soma == float):
        print("A soma dos numero é decimal")

elif (op == "Subtração") or (op == "Subtracao") or (op == "subtracao") or (op == "subtração"):
    subtracao = n1 - n2
    p_i = subtracao % 2

    if(p_i == 0):
        print("A subtração dos numero é par! ")

    elif(p_i == 1):
        print("A subtração dos numero é impar!")
    
    if(subtracao >= 0): 
        print("A subtração dos numero é positivo!")

    elif(subtracao <= -1):
        print("A subtração dos numero é negativo!")

    if (subtracao == int):
        print("A subtração dos numero é inteiro!")
    
    elif (subtracao == float):
        print("A subtração dos numero é decimal")

elif (op == "Multiplicação") or (op == "Multiplicacao") or (op == "multiplicação") or (op == "multiplicacao"):
    multiplicacao = n1 * n2
    p_i = multiplicacao % 2

    if(p_i == 0):
        print("A multiplicação dos numero é par! ")

    elif(p_i == 1):
        print("A multiplicação dos numero é impar!")
    
    if(multiplicacao >= 0): 
        print("A multiplicação dos numero é positivo!")

    elif(multiplicacao <= -1):
        print("A multiplicação dos numero é negativo!")

    if (multiplicacao == int):
        print("A multiplicação dos numero é inteiro!")
    
    elif (multiplicacao == float):
        print("A multiplicação dos numero é decimal")

elif (op == "Divisão") or (op == "divisão") or (op == "divisão") or (op == "divisao"):
    divisao = n1 / n2
    p_i = divisao % 2

    if(p_i == 0):
        print("A divisão dos numero é par! ")

    elif(p_i == 1):
        print("A divisão dos numero é impar!")
    
    if(divisao >= 0): 
        print("A divisão dos numero é positivo!")

    elif(divisao <= -1):
        print("A divisão dos numero é negativo!")

    if (divisao == int):
        print("A divisão dos numero é inteiro!")
    
    elif (divisao == float):
        print("A divisão dos numero é decimal")