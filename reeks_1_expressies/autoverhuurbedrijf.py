# Invoer
## De decimale getallen $b$, $e$ en $l$, in die volgorde en op drie afzonderlijke regels.
kilometerteller_aanvang = float(input()) #b
kilometerteller_terug = float(input()) #e
liter_benzine = float(input()) #l

# Uitvoer
## Het benzineverbruik van de auto, in liter per honderd kilometer.

if kilometerteller_aanvang < 0 or kilometerteller_terug < 0 or liter_benzine < 0:
    print('geef drie geldige getallen in!')
else:
    afstand = kilometerteller_terug - kilometerteller_aanvang
    verbruik = liter_benzine / afstand * 100
    print(verbruik)
