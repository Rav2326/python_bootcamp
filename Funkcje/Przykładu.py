#
# def nazwa(a):
#     """
#     Return '-' times a
#     example:
#     >>> nazwa(10)
#     '__________'
#
#     :param a:
#     :return:
#     """
#     return "-"*a
#
# print(nazwa(1))
# print(nazwa(10))
# print(nazwa(20))
# print(nazwa(30))
# print()
#
#
#
#__________________________________
# print(nazwa)
# print(type(nazwa))
# print(type(nazwa(2)))

# a= 5
# b = "Tort"
#
# def wieksze_niz_w(a):
#     if a > 2:
#         return True
#     return False
#
# def nazwa(a):
#     """
#     Return '-' times a
#     example:
#     >>> nazwa(10)
#     '__________'
#
#     :param a:
#     :return:
#     """
#     return "-"*a
#
# print(nazwa(1))
# print(nazwa(10))
# print(nazwa(20))
# print(nazwa(30))
# print()
# print(nazwa)
# print(type(nazwa))
# print(type(nazwa(2)))
# a= 5
# b = "Tort"
#
# def wieksze_niz_w(a):
#     if a > 2:
#         return True
#     return False
#__________________________
# def foo(x):
#     if x == 100:
#         return x
#     else:
#         print(x)
#         foo(x+1)
#
# foo(1)
#____________________________-
# def silnia(x):
#     if x == 0:
#         return 1
#     return x * silnia(x-1)
#
# def test_silnia():
#     assert silnia(3) == 6
#     assert silnia(0) == 1
#______________________________
def reku_print(x):
    if len(x) == 1:
        print(x[0])
    else:
        print(x[0])
        reku_print(x[1:])

    print(x[0])
    reku_print(x[1:])

reku_print([1, 2, 3])