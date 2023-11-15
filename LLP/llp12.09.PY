def main():
    nomes = []

    while True:
        nome = input("Digite um nome (ou digite 'q' para parar): ")
        
        if nome.lower() == 'q':
            break
        
        nomes.append(nome)

    nomes.sort()

    print("Nomes em ordem alfabética:")
    for nome in nomes:
        print(nome)

if __name__ == "__main__":
    main()