opties = ["blad", "steen", "schaar", "hagedis", "spock"]

invoer1 = input().lower()
invoer2 = input().lower()

if invoer1 not in opties or invoer2 not in opties:
    print(f'kies uit {", ".join(opties)}')
else:
# gelijkspel bij gelijke input
    if invoer1 == invoer2:
        print('gelijkspel')

# schaar snijdt blad
    elif invoer1 == "schaar" and invoer2 == "blad":
        print('speler1 wint')
    elif invoer2 == "schaar" and invoer1 == "blad":
        print('speler2 wint')
        
# blad bedekt steen
    elif invoer1 == "blad" and invoer2 == "steen":
        print('speler1 wint')
    elif invoer2 == "blad" and invoer1 == "steen":
        print('speler2 wint')

# steen plet hagedis
    elif invoer1 == "steen" and invoer2 == "hagedis":
        print('speler1 wint')
    elif invoer2 == "steen" and invoer1 == "hagedis":
        print('speler2 wint')

# hagedis vergiftigt spock
    elif invoer1 == "hagedis" and invoer2 == "spock":
        print('speler1 wint')
    elif invoer2 == "hagedis" and invoer1 == "spock":
        print('speler2 wint')

# spock smelt schaar
    elif invoer1 == "spock" and invoer2 == "schaar":
        print('speler1 wint')
    elif invoer2 == "spock" and invoer1 == "schaar":
        print('speler2 wint')

# schaar onthoofdt hagedis
    elif invoer1 == "schaar" and invoer2 == "hagedis":
        print('speler1 wint')
    elif invoer2 == "schaar" and invoer1 == "hagedis":
        print('speler2 wint')

# hagedis eet blad
    elif invoer1 == "hagedis" and invoer2 == "blad":
        print('speler1 wint')
    elif invoer2 == "hagedis" and invoer1 == "blad":
        print('speler2 wint')

# blad weerlegt spock
    elif invoer1 == "blad" and invoer2 == "spock":
        print('speler1 wint')
    elif invoer2 == "blad" and invoer1 == "spock":
        print('speler2 wint')

# spock verdampt steen
    elif invoer1 == "spock" and invoer2 == "steen":
        print('speler1 wint')
    elif invoer2 == "spock" and invoer1 == "steen":
        print('speler2 wint')

# steen breekt schaar
    elif invoer1 == "steen" and invoer2 == "schaar":
        print('speler1 wint')
    elif invoer2 == "steen" and invoer1 == "schaar":
        print('speler2 wint')