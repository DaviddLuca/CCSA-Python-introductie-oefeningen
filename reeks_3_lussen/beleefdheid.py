n = int(input())

beleefdheid = 0
start = 1

while start * 2 < n + 1:
    som = 0
    getal = start
    while som < n:
        som += getal
        getal += 1
    if som == n and getal - start >= 2:
        beleefdheid += 1
    start += 1
print(beleefdheid)