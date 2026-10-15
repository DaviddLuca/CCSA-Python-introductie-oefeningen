aantal_gekochte_stuks = int(input())
kostprijs_per_stuk = float(input())
aantal_barcodes = int(input())
aantal_mijlen = int(input())

if aantal_gekochte_stuks < 0 or aantal_barcodes < 0 or aantal_mijlen < 0 or kostprijs_per_stuk < 0:
    print('geen natuurlijk getal')
else:
    bedrag = aantal_gekochte_stuks * kostprijs_per_stuk
    mijlen = (aantal_gekochte_stuks // aantal_barcodes) * aantal_mijlen   
    print(f"Phillips spendeerde ${bedrag} voor {mijlen} frequent flyer mijlen.")