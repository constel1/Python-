# # a = 1,2
# # print(a)
# # x,y = a
# # print(x,y)
# a,b = "ra"
# print(a,b)
# a = (1,2,3)
# print(len(a))
# print(a[0])
# d = {}
# d[a] = "кортеж"
# print(d)
# import time
#
#
# # def get_sqrt(x):
# #     res = None if x < 0 else x ** 0.5
# #     return res, x
# #
# #
# # a = get_sqrt(49)
# # print(a)
#
# def maxim(a, b):
#     return a if a > b else b
#
#
# def get_nod(a, b):
#     if a<b:
#         a,b = b,a
#
#     while b!=0:
#         a,b = b, a%b
#     return a
#
#
# def test_nod(func):
#     # ------- test №1 -------
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print("#test1 - Ok")
#     else:
#         print("#test1 - fail")
#
#     # ------- test №2 -------
#     a = 100
#     b = 1
#     res = func(a, b)
#     if res == 1:
#         print("#test2 - Ok")
#     else:
#         print("#test2 - fail")
#     # ------- test №3 -------
#     a = 2
#     b = 100000000
#     st = time.time()
#     res = func(a,b)
#     et = time.time()
#     dt = et-st
#     if res ==2 and dt<1:
#         print("#test3 - Ok")
#     else:
#         print("#test2 - fail")
#
#
#
#
# # print(get_nod(18, 24))
# test_nod(get_nod)

# def recursive(value):
#     print(value)
#     recursive(value+1)
#
# recursive(1)
def fact(n):
    if n <=0:
        return 1
    return n*fact(n-1)

print(fact(6))


