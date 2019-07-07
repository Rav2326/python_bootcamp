# przyklad
# generator wywoalnyu kilka razy pamieta poprzedni stan
# oszczednosc pamieci
# pewien rodzaj funkcji (pod def)


# def kolejne_liuczby(n):
#     for i in range(n):
#         yield i**2
#
# print(list(kolejne_liuczby(10)))
# for liczba in kolejne_liuczby(10):
#     print(liczba)


# generator pascala

def gen_trojkat_pascala(n, r=[]):
    for x in range(n):
        length = len(r)
        # r = [l if i==0 or i == lengh else r[i-1] + r[i] for i in range(length+1)]
        temp = []
        for i in range(length+1):
            if i == 0 or i == length:
                temp.append(1)
            else:
                temp.append(r[i-1]+r[i])
        r = temp
        yield r
