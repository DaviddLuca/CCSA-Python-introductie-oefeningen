invoer = int(input())

if invoer < 1 or invoer > 9:
    print('geef een getal tussen 0 en 9')
else:
    for regel in range(1, invoer + 1):
        for cijfer in range(1, regel + 1):
            print(cijfer, end='')
        print()