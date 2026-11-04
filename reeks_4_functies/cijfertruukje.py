def even_oneven(getal):
    even = 0
    oneven = 0
    for cijfer in str(getal):
        if int(cijfer) % 2 == 0:
            even += 1
        else:
            oneven += 1
    return(even, oneven)

def volgende(getal):
    even, oneven = even_oneven(getal)
    totaal = even + oneven
    return int(str(even) + str(oneven) + str(totaal))

def stappen(getal):
    teller = 0
    while getal != 123:
        getal = volgende(getal)
        teller += 1
    return teller

# --- TEST ---
print(even_oneven(886328712442992))   # (10, 5)
print(even_oneven(145))               # (1, 2)
print(even_oneven(0))                 # (1, 0)

print(volgende(886328712442992))   # 10515
print(volgende(10515))             # 145
print(volgende(111))               # 33

print(stappen(886328712442992)) # 3 
print(stappen(0)) #2 (0 → 101 → 123)
print(stappen(1)) # 5
print(stappen(123)) # 0, want je bent er al