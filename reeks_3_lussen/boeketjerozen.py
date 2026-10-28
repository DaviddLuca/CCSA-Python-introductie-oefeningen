operators = ['>', '<']

aantal_rode_witte_rozen = int(input())
if aantal_rode_witte_rozen < 0:
    print('geef een natuurlijk getal')
else:
    aantal_witte_blauwe_rozen = int(input())
    if aantal_witte_blauwe_rozen < 0:
        print('geef een natuurlijk getal')
    else:
        operator = input()
        if operator not in operators:
            print('geef een geldige operator in')
        else:
            for w in range(2, min(aantal_rode_witte_rozen, aantal_witte_blauwe_rozen) + 1):
                r = aantal_rode_witte_rozen - w
                b = aantal_witte_blauwe_rozen - w

                if r < 2 or b < 2:
                    continue

                elif operator == '<':
                    geldig = b + r < w + b
                else:
                    geldig = b + r > w + b

                if geldig:
                    print(b)
                    print(w)
                    print(r)
                    break