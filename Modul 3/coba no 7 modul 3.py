from functools import reduce

angka = [1, 2, 3, 4, 5]

kuadrat = list(map(lambda x: x**2, angka))
print("Hasil kuadrat:", kuadrat)

genap = list(filter(lambda x: x % 2 == 0, angka))
print("Angka genap:", genap)

total = reduce(lambda x, y: x + y, angka)
print("Total:", total)