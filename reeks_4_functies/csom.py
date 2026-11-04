def csom(getal):
    while getal >= 10:
        totaal = 0
        for cijfer in str(getal):
            totaal += int(cijfer)
        getal = totaal
    return getal

print(csom(8)) #8
print(csom(377096267)) #2
print(csom(10)) #1