def waardering(prijs_BC, wisselkoers):
    prijs_VS = 4.07
    big_mac_koers = prijs_BC / prijs_VS
    verschil = (big_mac_koers - wisselkoers) / wisselkoers * 100
    if verschil <= -25:
        return "sterk ondergewaardeerd"
    elif -25 < verschil <= -5:
        return "ondergewaardeerd"
    elif -5 < verschil <= 5:
        return "ongeveer gelijk"
    elif 5 < verschil <= 25:
        return "overgewaardeerd"
    elif verschil > 25:
        return "sterk overgewaardeerd"
    

def wisselkoersanalyse(prijs_BC_euro, wisselkoers):
     delen = prijs_BC_euro.split(" ", 1)
     prijs = float(delen[0])
     munt = delen[1]
     return f"De {munt} is {waardering(prijs, wisselkoers)} ten opzichte van de dollar."

# - TEST -
print(waardering(3.44, 0.70))                     # overgewaardeerd
print(wisselkoersanalyse('3.44 euro', 0.70))      # De euro is overgewaardeerd ten opzichte van de dollar.
print(wisselkoersanalyse('2.39 pond sterling', 0.62)) # De pond sterling is ondergewaardeerd ten opzichte van de dollar.