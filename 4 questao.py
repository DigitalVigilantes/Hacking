alturas = []
for i in range(15):
    while True:
        altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
        if 0.4 <= altura <= 2.6:
            alturas.append(altura)
            break

print(f"Maior altura: {max(alturas)}")
print(f"Menor altura: {min(alturas)}")