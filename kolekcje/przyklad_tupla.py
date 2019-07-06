zmienna1 = 100
my_tuple = (1, 2, 3, 'a', 'b', 'a' , 'c', zmienna1)
print(my_tuple)
#print(dir(my_tuple))
print(my_tuple.count('a'))
print(my_tuple.index('a'))
print(my_tuple[3])
print(my_tuple[1:6]) #od 1 do 6 (0 tez sie liczy)
print(my_tuple[1:8:2]) # od 1 do 8 co 2 krok
print(my_tuple[::2]) #co drugi

t1 = (1, 2, 3)
#print(id(t1))
t2 = (4, 5, 6)

print(t1 + t2)
#print(id(t1))


# pusta tupla:

print(type(my_tuple))

x = tuple()
print(tuple(range(10)))