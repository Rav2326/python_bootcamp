
f = open("data.txt", "rt")
print("Czy zamkniety = {}".format(f.closed))                 # Wariant 1
f.close()
print("Czy zamkniety = {}".format(f.closed))

print("-----------------------")

with open ("data.txt", "rt") as f:
    print("Czy zamkniety = {}".format(f.closed))           # Wariant 2 (najlepszy)
print("Czy zamkniety = {}".format(f.closed))

print("------------------")

f = None

try:
    f = open("data.txt", "rt")                              # Wariant 3 
except Exception as e:
    print(str(e))
finally:
    if f is not None:
        f.close()


