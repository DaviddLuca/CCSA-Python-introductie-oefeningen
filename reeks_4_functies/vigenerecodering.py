def codeer(tekst, sleutel):
    resultaat = ""
    for i in range(len(tekst)):
        teken = tekst[i]
        if teken.isupper():
            sleutelletter = sleutel[i % len(sleutel)]
            getal_teken = ord(teken) - ord("A")
            getal_sleutel = ord(sleutelletter) - ord("A")
            nieuw = (getal_sleutel + getal_teken) % 26
            resultaat += chr(nieuw + ord("A"))
        else:
            resultaat += teken
    return resultaat

def decodeer(tekst, sleutel):
    resultaat = ""
    for i in range(len(tekst)):
        teken = tekst[i]
        if teken.isupper():
            sleutelletter = sleutel[i % len(sleutel)]
            getal_teken = ord(teken) - ord("A")
            getal_sleutel = ord(sleutelletter) - ord("A")
            nieuw = (getal_teken - getal_sleutel) % 26
            resultaat += chr(nieuw + ord("A"))
        else:
            resultaat += teken
    return resultaat

# --- TEST ---
print(codeer('N', 'C'))   # P
print(codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS'))
# PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!
print(codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR'))
# OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!

print(decodeer('E', 'B'))   # D
print(decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS'))
# NOBODY EXPECTS THE SPANISH INQUISITION!
print(decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR'))
# OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!