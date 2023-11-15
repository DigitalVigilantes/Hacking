def kmp(dna, protein, queries):
    n = len(dna)
    m = len(protein)
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and protein[i] != protein[j]:
            j = prefix[j - 1]
        if protein[i] == protein[j]:
            j += 1
        prefix[i] = j
    results = []
    for a, b in queries:
        subprotein = protein[a - 1:b]
        k = b - a + 1
        j = 0
        count = 0
        for i in range(n):
            while j > 0 and dna[i] != subprotein[j]:
                j = prefix[j - 1]
            if dna[i] == subprotein[j]:
                j += 1
            if j == k:
                count += 1
                j = prefix[j - 1]
        results.append(count)
    return results


dna = 'AAACAACTGA'
protein = 'CGGACAA'
queries = [(1, 1), (2, 7), (5, 7), (6, 7), (4, 5), (6, 6)]
print(kmp(dna, protein, queries))