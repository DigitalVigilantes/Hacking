def main():

    nomes = []
    notas = []

    num_alunos = int(input("Digite o número de alunos: "))

    for i in range(num_alunos):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))

        nomes.append(nome)
        notas.append(nota)

    total_notas = sum(notas)
    media = total_notas / num_alunos

    print(f"A média das notas dos alunos é: {media:.2f}")

if __name__ == "__main__":
    main()
  