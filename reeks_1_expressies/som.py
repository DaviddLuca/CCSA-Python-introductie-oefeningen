getal1 = int(input())
getal2 = int(input())

if getal1 < 0 or getal2 < 0:
    print('Geen geldig getal!')
else:
    print(getal1 + getal2)

# testen werken NIET
# try: 
#     getal1 = float(input('Geef getal 1: '))
#     getal2 = float(input('Geef getal 2: '))
#     if getal1 < 0 or getal2 < 0:
#         raise ValueError
#     sum = getal1 + getal2

# except ValueError:
#     print('Fout! Geef aub een geheel getal in')
# except Exception as error:
#     print(error)
# else:
#     print(sum)