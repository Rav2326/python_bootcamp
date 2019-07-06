moja_lista = [1, 2, 3, "a", "b", "c"]
print(type(moja_lista))
#print(dir(moja_lista))

moja_lista.append(5)
print(moja_lista)

moja_lista.append([5, 6, 7])
print(moja_lista)

print(help(moja_lista.insert))
moja_lista.insert(1, "d")
print(moja_lista)

print([1, 2, 3] + [7, 8 ,9])

c = [9, 1, 5, 3, 2]

c.sort()
print(c)

print(c.pop())
print(c)
d = [1, 2, 3]

d.extend([5,6,7])
print(d)

#for

moja_lista = [1, 2, 3, "a", "b", "c"]