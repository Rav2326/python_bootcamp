
import pickle

x= 42
y = 12.3456
s = "Ala ma kota i jest rudy"
l = [0, 2, "A", 99.99, True]

print(f"x = {x}")
print(f"x = {y}")
print(f"x = {s}")
print(f"x = {l}")

DUMP_FILE = "save.bin"

with open(DUMP_FILE, "wb")as f:                  #marynujemy zmienne
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(s, f)
    pickle.dump(l, f)

print("=====================")

with open(DUMP_FILE, "rb") as f:                   #odmarynowane zmienne
    x1 = pickle.load(f)
    y1 = pickle.load(f)
    s1 = pickle.load(f)
    l1 = pickle.load(f)
    print(f"x = {x1}")
    print(f"x = {y1}")
    print(f"x = {s1}")
    print(f"x = {l1}")