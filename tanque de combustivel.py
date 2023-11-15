C = int(input())
D = int(input())
T = int(input())

fuel_needed = D / C
fuel_to_buy = max(0, round(fuel_needed - T, 1))

print(fuel_to_buy)