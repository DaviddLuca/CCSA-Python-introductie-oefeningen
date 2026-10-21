invoer1 = input()
invoer2 = input()


# Eerste weging: eerste muntstuk van de verdachte groep (1, 4 of 7)
if invoer1 == "links":
    begin = 4
elif invoer1 == "rechts":
    begin = 1
else:
    begin = 7

# Tweede weging: plaats in de groep (0, 1 of 2)
if invoer2 == "links":
    positie = 1
elif invoer2 == "rechts":
    positie = 0
else:
    positie = 2

n = begin + positie

print(f'muntstuk #{n} is vervalst')