alunos =[]
while True:
    nome = input("Digite o nome do(a) aluno(a): ")
    alunos.append(nome)

    resp = input ("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break
for nome in alunos:
    print(nome)