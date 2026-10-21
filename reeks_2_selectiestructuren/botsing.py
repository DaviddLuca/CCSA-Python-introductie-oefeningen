# - Invoer -
# De invoer bestaat uit acht gehele getallen (één per regel) die tweemaal twee diametrale punten van twee rechthoeken voorstellen. 
getal1 = int(input())
getal2 = int(input())
getal3 = int(input())
getal4 = int(input())
getal5 = int(input())
getal6 = int(input())
getal7 = int(input())
getal8 = int(input())

#punten
punt1 = (getal1, getal2)
punt2 = (getal3, getal4)
punt3 = (getal5, getal6)
punt4 = (getal7, getal8)

# Rechthoek1
links1 = min(punt1[0], punt2[0])
rechts1 = max(punt1[0], punt2[0])
onder1 = min(punt1[1], punt2[1])
boven1 = max(punt1[1], punt2[1])

# Rechthoek2
links2 = min(punt3[0], punt4[0])
rechts2 = max(punt3[0], punt4[0])
onder2 = min(punt3[1], punt4[1])
boven2 = max(punt3[1], punt4[1])


#controle
if rechts1 <= links2 or rechts2 <= links1 or boven1 <= onder2 or boven2 <= onder1:
    print("geen botsing")
else:
    print("botsing")