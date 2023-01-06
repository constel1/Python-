# # d = [3,5,25,6,96,34]
# # it = iter(d)
# # for i in range(len(d)):
# #     print(next(it))
# # r = range(4)
# # it = iter(r)
# # for i in r:
# #     print(next(it))
# a = [[1,2,3], [4,5,6], [7,8,9]]
# b = [[1,1,1], [2,2,2], [3,3,3]]
# # for x in a:
# #     for z in x:
# #         print(z, end=" | ")
# #     print()
# #     print("-----------")
# # print()
# # for x in b:
# #     for z in x:
# #         print(z, end=" | ")
# #     print()
# #     print("-----------")
# c = []
# for i, row  in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x+b[i][j])
#     c.append(r)
# # print()
# # print(c)
# #
# # print()
# #
# # for x in c:
# #     for z in x:
# #         print(z, end=" | ")
# #     print()
# #     print("-----------")
# t = ["- Скажика дядя ведь не даром",
#      "Я Python выучил с  каналом",
#      "Балакирев что  раздавал ",
#      "Ведь были  ж  задания боевые,",
#      "Да говорят  ещё  какие",
#      "Недаром  помнит вся Россия",
#      "Как мы рубили их тогда"]
# # print("\n".join(t))
# # print("\n-------------\n")
# # print(("\n".join(t)).replace("  ", " "))
# for i, line in enumerate(t):
#     while line.count("  "):
#         line = line.replace("  ", " ")
#     t[i] = line
# #m,n = list(map(int, input("Введите M и N: ").split()))
#
#
# n,m = list(map(int, input("Введите M и N: ").split()))
# print(n, m)
# # zeros = []
# # for i in range(m):
# #     zeros.append([0]*n)
# # print(zeros)
# arr = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(arr)
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
# print(arr)



















