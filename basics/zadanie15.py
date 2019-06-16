min_l = None
max_l = None
while True:
    x = input("Wpisz liczbę lub k by zakończyć")
    if x == 'k':
        break
    x = int (x)
    if min_l is None or x < min_l:
        min_l=x
    if max_l is None or x > max_1:
        max_1=x


