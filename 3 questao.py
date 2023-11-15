alturas = []
for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
    alturas.append(altura)

print(f"Maior altura: {max(alturas)}")
print(f"Menor altura: {min(alturas)}")