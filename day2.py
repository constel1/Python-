
# # def key_sort(x):
# #     return x if x%2==0 else x+100
# # a = [4,3,-10,1,7,12]
# # b= sorted(a,key=key_sort)
# # print(b)
# lst = ["Москва", "Тверь", "Смоленск", "Псков","Рязань"]
# b = sorted(lst, key=lambda x:x[0])
# print(b)
# b = sorted(lst, key=lambda x:x[0], reverse=True)
# print(b)
# a = 98
# print(isinstance(a, int))
# data = [4.5, 8.7, True, "книга", 8,10,-23,[True,False]]
# s = sum(filter(lambda x:isinstance(x,float),data))
# print(s)
# a = [0,1, [], "",0]
# all_res = False
# for x in a:
#     all_res =all_res or  bool(x)
# #print(all_res)
# s = ["*", 0,5]
# #print(False or True)
# d = map(lambda x:x=="*",s)
# print(next(d))
# print(next(d))
# print(next(d))
# import random
# # a = random.gauss(0,5)
# # print(a)
# lst = [4,5,0,-1,10,76,3]
#
# a = random.choice(lst)
# random.shuffle(lst)


from typing import Final
a: Final =3
b: Final =5
cmd = 3




