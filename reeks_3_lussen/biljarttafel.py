# invoer : de hoogte en breedte van de tafel
h = int(input())
b = int(input())

# beginpositie: linkeronderhoek
x, y = 0, 0

# richting: 1 stap naar rechts en 1 stap omhoog (hoek van 45°)
dx, dy = 1, 1

while True:
    # de bal verplaatst zich 1 stap in zijn huidige richting
    x += dx
    y += dy

    # controleer eerst of de bal in een hoek zit: dan verdwijnt hij in een pocket
    if x in (0, b) and y in (0, h):
        kant = 'linker' if x == 0 else 'rechter'
        hoek = 'onder' if y == 0 else 'boven'
        print(f'{kant}{hoek}pocket ({x}, {y})')
        break
    # anders raakt de bal een band: schrijf de band uit en keer de richting om
    elif x == 0:
        print(f'linkerband ({x}, {y})')
        dx = 1      # na de linkerband gaat de bal naar rechts
    elif x == b:
        print(f'rechterband ({x}, {y})')
        dx = -1     # na de rechterband gaat de bal naar links
    elif y == 0:
        print(f'onderband ({x}, {y})')
        dy = 1     # na de onderband gaat de bal omhoog
    elif y == h:
        print(f'bovenband ({x}, {y})')
        dy = -1     # na de bovenband gaat de bal omhoog