#Em uma turma de alunos que conversavam muito, um professor montou a seguinte estratégia: após os alunos se sentarem, ele mandava os alunos trocarem de lugar.

#Para ajudar esse processo, crie um programa para ajudar esse professor. O programa deve ler um valor N, que representa a quantidade de alunos. Em seguida, deve ler os nomes de cada aluno e armazená-los em uma lista. Considere a sequência lida como a ordem das cadeiras dos alunos.

#O programa deve então imprimir os nomes em uma nova ordem, trocando os alunos sentados em cadeiras de número par (o da primeira cadeira par vai para a última par, o da segunda para a antepenúltima, etc.).

#Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, vão haver 3 cadeiras pares), o aluno da cadeira central não terá seu local trocado.

N = int(input("Quantos alunos: "))

print("Digite os nomes dos alunos: ")
alunos = [input() for _ in range(N)]

pares = [i for i in range(1, N, 2)]

pares_reversos = pares[::-1]
for i in range(len(pares)):
    alunos[pares[i]] = alunos[pares_reversos[i]]

print("Nova lista: ")
for aluno in alunos:
    print(aluno)