zijde = input()
tekst = input()
antwoord = input()

if zijde == "waarde":
    getal = int(tekst)
    moet_draaien = getal % 2 == 0
else:
    moet_draaien = tekst != "rood"  
zegt_ja = antwoord == "ja"
if moet_draaien == zegt_ja:
    resultaat = "Juist"
else:
    resultaat = "Fout"

if moet_draaien:
    gedraaid = "gedraaid"
else:
    gedraaid = "niet gedraaid"

print(f"{resultaat}: kaarten met {zijde} {tekst} moeten {gedraaid} worden.")