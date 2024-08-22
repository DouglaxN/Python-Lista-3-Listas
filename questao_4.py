#Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno e imprimí-los na ordem inversa.

#OBS.: os nomes devem ser armazenados em uma lista para depois imprimir na ordem inversa.

quantidade_alunos = int(input("Quantos nomes? "))

nomes = []
for _ in range(quantidade_alunos):
    nome = input()
    nomes.append(nome)

print("Você digitou: ")

for nome in reversed(nomes):
    print(nome)
