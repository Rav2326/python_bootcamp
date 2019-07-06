napis = "Ala ma <kota>, a kot ma Alę"

nawias = napis.index[8, 13]
ile = 0

for nawias in napis.lower():
    if nawias in napis:
        ile +=  1

print(f"W nawiasie jest {ile} liter")