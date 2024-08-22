#Crie um programa que lê um valor numérico N e 
#que em seguida lê N números. Armazene esses números em uma lista. 
#Em seguida, leia do usuário 3 números inteiros (OP, A e B). 
#O primeiro número (OP) representa uma operação matemática (0 é soma, 1 é multiplicação) 
#que deve ser realizada em cima dos dois números cujas posições (1 a N) na lista são A e B. 
#O programa deve então apresentar a operação e seu resultado.

N = int(input("Qual o N? "))

numeros = []
print("Digite os valores: ")
for _ in range(N):
    numeros.append(int(input()))

OP = int(input("Qual o op? "))
A = int(input("Qual o A? "))
B = int(input("Qual o B? "))

A -= 1
B -= 1

if 0 <= A < N and 0 <= B < N:
    valor_A = numeros[A]
    valor_B = numeros[B]

    if OP = 0:
        resultado = valor_A + valor_B
        opracao = f"{valor_A + valor_B}"
    elif OP == 1:
        resultado = valor_A * valor_B
        operacao = f"{valor_A} * {valor_B}"
    else:
        operacao = "Operação inválida"
        resultado = None

    if resultado is not None:
        print(f"{operacao} = {resultado}")
    else:
        print(operacao)
else:
    print("Índices fora do intervalo.")
