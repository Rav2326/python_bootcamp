lista = [9,1,6,8,4,3,2,0]

for i in range (len(lista)):
    print( i, lista[i:])  #wylacz ciag dalszy i zrozum tę część

    min_v = lista[i:][0] #miniwalna wartosc
    i_min_v = 0          #index minimalnej wartosci
    for j in lista[i:]:
        if j < min_v:
            min_v = j
            i_min_v = lista[i:].index(j)

    #temp = lista[i]  #chwilowe ukrycie cyfr
    #lista[i] = lista[i + i_min_v]
    #lista[i +i_min_v] = temp

    lista[i], lista[i+i_min_v] = lista[i+i_min_v] , lista[i]

    lista[i] = lista[i+i_min_v]     #zeby lista sie nie skracala
    print("Po zmianie: ", lista)
    print("znalezione min to: ", min_v, i_min_v)