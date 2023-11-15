def maior_prefixo_comum(palavra1, palavra2):
    n = len(palavra1)
    m = len(palavra2)
    min_len = min(n, m)
    
    for i in range(min_len):
        if palavra1[i] != palavra2[i]:
            return i
    return min_len

n = int(input())
palavra1 = input()
m = int(input())
palavra2 = input()

resultado = maior_prefixo_comum(palavra1, palavra2)

print(resultado)