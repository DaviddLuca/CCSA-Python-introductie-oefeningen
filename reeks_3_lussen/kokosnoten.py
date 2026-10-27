# invoer
p = int(input())
k = int(input())

def noten(aantal):
    if aantal == 0:
        return 'geen noten'
    elif aantal == 1:
        return '1 noot'
    return f'{aantal} noten'

hoop = k
for n in range(1, p + 1):
    verstopt = hoop // p
    aap = hoop % p
    print(f'{noten(hoop)} = {noten(verstopt)} voor piraat#{n} en {noten(aap)} voor de aap')
    hoop = hoop - verstopt - aap

per_piraat = hoop // p
aap = hoop % p
print(f'elke piraat krijgt {noten(per_piraat)} en {noten(aap)} voor de aap')
