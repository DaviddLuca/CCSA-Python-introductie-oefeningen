invoer_uur_start = int(input())
invoer_min_start = int(input())
invoer_uur_eind = int(input())
invoer_min_eind = int(input())

start = invoer_uur_start * 60 + invoer_min_start
eind = invoer_uur_eind * 60 + invoer_min_eind

# grenzen in minuten
begin_goedkoop = 18 * 60
grens = 21 * 60 + 30
einde_dag = 24 * 60

if start < begin_goedkoop or eind > einde_dag or eind <= start:
    print("ongeldige invoer")
else:
    goedkoop = max(0, min(eind, grens) - start)
    duur = max(0, eind - max(start, grens))

    bedrag = goedkoop / 60 * 2 + duur / 60 * 4
    print(bedrag)