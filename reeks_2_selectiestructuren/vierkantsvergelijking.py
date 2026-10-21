# imports
import math

a = float(input())
b = float(input())
c = float(input())

# geen reële wortels als b² - 4ac < 0
driehoek = b*b - 4 * (a*c)

# één reële wortel, namelijk x = -(b/2*a) 
x = -(b/(2*a))


if driehoek < 0:
    print("geen wortels")
elif driehoek == 0:
    print("een wortel")
    print(x)
elif driehoek > 0:
    # twee reële wortels
    x1 = (-(b+math.sqrt(driehoek))/(2*a))
    x2 = (-(b-math.sqrt(driehoek))/(2*a))
    print("twee wortels")
    print(round(min(x1, x2), 6))
    print(round(max(x1, x2), 6))
else:
    print("er ging iets mis")