# Concreet moet de functie de waarde -1 teruggeven indien het gegeven geluidsniveau minder dan 80 dB bedraagt 
# (deze waarde correspondeert met een onbeperkte tijdsduur). 
# Voor een gegeven geluidsniveau binnen het interval [80, 83[ dB 
# moet de functie een waarde teruggeven die correspondeert met een tijdsduur van 8 uur. 
# Voor elk volgend geluidsinterval van 3 dB moet deze tijdsduur telkens gehalveerd worden 
# ([83, 86[ -> 4 uur, [86, 89[ -> 2 uur, [89, 92[ -> 1 uur, …).

def maximale_blootstelling(decibel):
    if decibel < 80:
        return float(-1)
    else:
        n = (decibel - 80) // 3
        uren = 8 / 2 ** n
        seconden = uren * 3600
    return float(seconden)


# - Testen -
print(maximale_blootstelling(40))
print(maximale_blootstelling(60))
print(maximale_blootstelling(75))
print(maximale_blootstelling(80))
print(maximale_blootstelling(86))
print(maximale_blootstelling(90))
print(maximale_blootstelling(95))
print(maximale_blootstelling(97))
print(maximale_blootstelling(105))
print(maximale_blootstelling(107))
print(maximale_blootstelling(118))
print(maximale_blootstelling(115))
print(maximale_blootstelling(120))