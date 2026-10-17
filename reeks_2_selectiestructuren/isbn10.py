getallen = []

# 1. getallen inlezen en controleren
while len(getallen) < 10:
    getal = int(input())
    if 0 <= getal <= 9:
        getallen.append(getal)
    else:
        print('geef een getal tussen 0 en 9')

# 2. bereken 
som = 0
for i in range(9):
    som += (i + 1) * getallen[i]
x10 = som % 11

# 3. vergelijken met geldig isbn10
if x10 == getallen[9]:
    print('OK')
else:
    print('FOUT')