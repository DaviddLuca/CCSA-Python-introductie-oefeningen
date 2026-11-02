def bovensteboven(getal):
    string_getal = str(getal)
    draai = {"6": "9", "9": "6", "8": "8", "0": "0", "1": "1"}
    gedraaid = ""
    for cijfer in string_getal:
        if cijfer not in draai:
            return False
        gedraaid += draai[cijfer]
    return gedraaid[::-1] == string_getal

def volgende(n):
    n = n + 1
    while not bovensteboven(n):
        n += 1
    return n

print(bovensteboven(689))    # True
print(bovensteboven(1961))   # True
print(bovensteboven(2965))   # False
print(bovensteboven(68089))  # True
print(bovensteboven(90306))  # False

print(volgende(689))         # 808
print(volgende(1961))        # 6009
print(volgende(98765))      # 98886