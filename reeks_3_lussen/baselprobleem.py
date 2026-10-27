from math import pi

doel = pi ** 2 / 6

# eerste regel: f_100
f = 0
for i in range(1, 101):
    f += 1 / i ** 2
print(f)

# tweede regel: kleinste n met |f_n - pi^2/6| <= 1/100
f = 0
n = 0
while abs(f - doel) > 1 / 100:
    n += 1
    f += 1 / n ** 2
print(n)