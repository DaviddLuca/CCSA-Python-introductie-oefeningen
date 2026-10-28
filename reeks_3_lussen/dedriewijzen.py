# het bedrah omzetten nzzr een tekst met twee cijfers na de komma
def euro(cent):
    return f'€{cent // 100}.{cent % 100:02d}'

# invoer: totaalbedrag, omgezet naar cent
t = round(float(input()) * 100)

# a + b + c = t (in cent)
# a * b * c = t in euro, dus in cent: A * B * C = t * 10000
product = t * 10000

def zoek(t, product):
    for a in range(1, t // 3 + 1):
        if product % a != 0:
            continue
        for b in range(a, (t - a) // 2 + 1):
            c = t - a - b
            if a * b * c == product:
                return a, b, c

a, b, c = zoek(t, product)
print(f'{euro(a)} + {euro(b)} + {euro(c)} = {euro(a)} x {euro(b)} x {euro(c)} = {euro(t)}')