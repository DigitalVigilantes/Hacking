def verificar_bem_definida(cadeia):
    pilha = []

    for caractere in cadeia:
        if caractere in '([{':
            pilha.append(caractere)
        elif caractere in ')]}':
            if len(pilha) == 0:
                return False
            
            ultimo_caractere = pilha.pop()
            if (ultimo_caractere == '(' and caractere != ')') or \
               (ultimo_caractere == '[' and caractere != ']') or \
               (ultimo_caractere == '{' and caractere != '}'):
                return False

    return len(pilha) == 0


num_instancias = int(input())

for _ in range(num_instancias):
    cadeia = input()
    if verificar_bem_definida(cadeia):
        print('S')
    else:
        print('N')
