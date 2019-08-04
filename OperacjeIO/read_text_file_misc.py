
with open("data.txt", "rt") as f:
    f.seek(9)    # przemieszczasz sie od pewnego danego momentu w ktorej jestes (bitu, czyli litery)
    line = f.read(10) # czytasz od pewnego danego momentu w ktorej jestes (bitu, czyli litery)
    print(line)
    print("\nMoja pozycja to {}".format(f.tell())) #tell- sprawdzanie gdzie znajdujesz sie w pliku


