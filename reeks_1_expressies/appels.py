# - extra info -
# In een kist passen 20 appels, en op een pallet passen 35 kisten.
# hoeveel volledige palletten hij kan vullen,
# hoeveel volledige kisten hij kan vullen met de overgebleven appels,
# hoeveel appels er dan nog over blijven.

# - invoer -
# Het aantal appels dat de boer geplukt heeft.

aantal_appels = int(input())

if aantal_appels < 0:
    print('geef een geldig getal in')
else:
    # het aantal volledige palletten, 
    aantal_palletten = (aantal_appels // 20) // 35
    # het aantal volledige kisten met de overgebleven appels
    aantal_overgebleven_kisten = (aantal_appels // 20) % 35
    # en het aantal appels dat finaal overblijft 
    rest = aantal_appels % 20
    print(aantal_palletten)
    print(aantal_overgebleven_kisten)
    print(rest)

# - uitvoer -
# Drie afzonderlijke regels met op elke regel een natuurlijk getal: 
    # het aantal volledige palletten, 
    # het aantal volledige kisten met de overgebleven appels 
    # en het aantal appels dat finaal overblijft (in die volgorde).