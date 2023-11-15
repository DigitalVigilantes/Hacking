def verificar_baralho(cartas):
    naipes = {'C': 'Copas', 'E': 'Espadas', 'U': 'Ouros', 'P': 'Paus'}
    resultados = {}

    for naipe in naipes.values():
        resultados[naipe] = []

    for i in range(0, len(cartas), 3):
        carta = cartas[i:i+3]
        valor = carta[:2]
        naipe = carta[2]

        if valor in resultados[naipes[naipe]]:
            resultados[naipes[naipe]].append('erro')
        else:
            resultados[naipes[naipe]].append(valor)

    for naipe in naipes.values():
        cartas_presentes = resultados[naipe]
        num_cartas_presentes = len(cartas_presentes)
        num_cartas_faltantes = 13 - num_cartas_presentes

        if num_cartas_presentes == 13:
            resultados[naipe] = 0
        elif num_cartas_faltantes > 0:
            resultados[naipe] = num_cartas_faltantes
        else:
            resultados[naipe] = 'erro'

    return resultados

cartas = '11P01C02C01U02U03U04U'
resultado = verificar_baralho(cartas)

for naipe, valor in resultado.items():
    print(valor)
