def varkenswoord(engelsWoord):
    # controle klinkers
    klinkers = "aeiouAEIOU"
    i = 0
    while i < len(engelsWoord) and engelsWoord[i] not in klinkers:
        #controle qu
        if engelsWoord[i] == 'q' and i + 1 < len(engelsWoord) and engelsWoord[i+1] == "u":
            i += 2
        else:
            i += 1
    # resultaat vormen adhv klinkers
    if i == 0:
        resultaat = engelsWoord + "way"
    elif engelsWoord[0].isupper():
        verplaatst_deel = engelsWoord[0].lower() + engelsWoord[1:i]
        vervormd_woord = engelsWoord[i:] + verplaatst_deel + "ay"
        resultaat = vervormd_woord[0].upper() + vervormd_woord[1:]
    else:
        resultaat = engelsWoord[i:] + engelsWoord[:i] + "ay"
    return resultaat

def varkenslatijn(zin):
    resultaat = ""
    huidig_woord = ""

    for char in zin:
        if char.isalpha():
            huidig_woord += char
        else:
            if huidig_woord:
                resultaat += varkenswoord(huidig_woord)
                huidig_woord = ""
            resultaat += char

    if huidig_woord:
        resultaat += varkenswoord(huidig_woord)

    return resultaat

# ---TEST--
print(varkenswoord('egg'))      # 'eggway'
print(varkenswoord('Pig'))      # 'Igpay'
print(varkenswoord('Latin'))    # 'Atinlay'
print(varkenswoord('trash'))    # 'ashtray'
print(varkenswoord('quit'))     # 'itquay'
print(varkenswoord('BaNaNa'))   # 'ANaNabay'
print(varkenswoord('DNa'))      # 'AdNay'
print(varkenswoord('plover'))   # 'overplay'
print(varkenswoord('plunder'))  # 'underplay'

print(varkenslatijn('And now for something completely different!'))
# Andway ownay orfay omethingsay ompletelycay ifferentday!
print(varkenslatijn('Stwike him, centuwion, stwike him vewy wuffly'))
# Stwikeway imhay, entuwioncay, stwikeway imhay ewyvay ufflyway
print(varkenslatijn('Hello, World! Quick brown fox.'))
# Ellohay, Orldway! Uickquay ownay oxfay.