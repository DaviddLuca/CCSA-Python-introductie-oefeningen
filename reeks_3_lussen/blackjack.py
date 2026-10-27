# Vraag aan de gebruiker één voor één kaarten met een waarde van 1 tot en met 11. Het programma stopt met het vragen van kaarten in de volgende drie gevallen:

# Het totaal van de kaarten is 21. Toon de boodschap Gewonnen!.
# Het totaal van de kaarten is meer dan 21, bijvoorbeeld 24. Toon dan Verbrand (24).
# Het totaal van de kaarten is minder dan 21, bijvoorbeeld 19 en de gebruiker geeft een kaart met waarde 0. Toon Voorzichtig gespeeld (19).

totaal = 0

while totaal < 21:
    kaart = int(input())
    if kaart == 0:
        break
    elif kaart < 1 or kaart > 11:
        print('getal moet tussen de 1 en 11 zijn')
    else:
        totaal += kaart
    
if totaal == 21:
    print('Gewonnen!')
elif totaal > 21:
    print(f'Verbrand ({totaal})')
else:
    print(f'Voorzichtig gespeeld ({totaal})')