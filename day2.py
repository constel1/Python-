# # #
# # # a = []
# # # for i in range(int(input("сколько? - "))):
# # #     row = [1]*(i+1)
# # #     for j in range(i+1):
# # #         if j !=0 and j != i:
# # #             row[j] = a[i - 1][j - 1] + a[i - 1][j]
# # #
# # #     a.append(row)
# # #
# # # for i in a:
# # #     print(i)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # N =10
# # # a = [0]* N
# # # for i in range(N):
# # #     a[i] = i**2
# # a = [x**2 for x in range(N)]
# # print(a)
# # a = [1 for x in range(N)]
# # print(a)
# # a = [x%4 for x in range(N)]
# # print(a)
# # a = [x%2==0 for x in range(N)]
# # print(a)
# # a = [0.5*x +1 for x in range(N)]
# # print(a)
# # inp = list(map(int, input("введите целые числа через пробел - ").split()))
# # inp = input("введите целые числа через пробел - ")
# # a = [int(d) for d in inp.split()]
# # print(a)
# # a = [x for x in range(-5, 5) if x<0]
# # print(a)
# # cities = ['москва', "Владимир", "казань", "Владивосток", "Питер"]
# # a = [city for city in cities if len(city)<7]
# # print(cities)
# # print(a)
# def ar (arr1):
#     a = [x for x in arr1 if x%2==0]
#     b = [x for x in arr1 if x % 2 != 0]
#
#     return a,b
# d = [2,-45,5,34,-26,83,-147,-36,91]
# a,b = ar(d)
# print(a)
# print(b)
# # d = [2,-45,5,34,-26,83,-147,-36,91]
# # a = ["чётное" if x%2==0 else
# #      "нечётное" for x in d
# #      if x>0
# #      ]
# # print(a)
