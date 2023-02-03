# a, b,c,d = int(input()),int(input()),int(input()),int(input())
# if a<b:
#     a,b = b,a
# if c >d:
#     c,d = d,c
# list1 = [[0 for x in range(d-c+2)] for row in range(a-b+2)]
#
# q,w = c,b
# for i in range(a-b+2):
#     for j in range(d-c+2):
#         if i==0 and j==0:
#             list1[i][j] = ""
#             continue
#         if i==0:
#             list1[i][j] = c
#             c+=1
#         if j==0:
#             list1[i][j] = b
#             b+=1
#
# for i in range(a-w+2):
#     for j in range(d-q+2):
#         if i==0 or j==0:
#             continue
#         list1[i][j] = list1[0][j] * list1[i][0]
#
# for row in list1:
#     for x in row:
#         print(x, end="\t")
#     print()
# a,b = int(input()), int(input())
# while a%3!=0:
#     a+=1
# s=0
# count =0
# for i in range(a,b+1,3):
#     s+=i
#     count+=1
# print(s/count)
# s = input()
# print( (s.upper().count("g".upper()) + s.upper().count("c".upper()))/len(s)*100)
# s = input()
# l = [s for s in s]
#
# count=0
# a=l[0]
# for i in range(len(l)):
#     if a==l[i]:
#         count+=1
#         if i!=(len(l)-1):
#             continue
#
#
#     print(f"{l[i-1]}{count}",end="")
#     a = l[i]
#     count=1
#     if i==len(l)-1 and l[i]!=l[i-1]:
#         print(f"{l[i]}{count}", end="")

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
# a = [1, 2, 3]
# b = a
# print(f"a - {a}\nb - {b}")
#
# a[1] = 10
# print(f"a - {a}\nb - {b}")
#
# b[0] = 20
# print(f"a - {a}\nb - {b}")
#
# a = [5, 6]
# print(f"a - {a}\nb - {b}")
# l = [int(x) for x in input().split()]
# #l1 = [ l[x+1]+l[x-1] if x!=0 or x!=len(l)-1 else l[x-1]+l[0] if x == len(l)-1 else l[-1]+l[x+1]for x in range(len(l))]
# l1 = []
#
#
# for i in range(len(l)):
#     if 0<i<len(l)-1:
#         l1.append(l[i+1]+l[i-1])
#
#
#     elif i == len(l)-1:
#         if len(l) == 1:
#             l1.append(l[0])
#             break
#         l1.append(l[i - 1] + l[0])
#
#     elif i == 0:
#         l1.append(l[-1] + l[i + 1])
#
#1 1 2 2 3 3
#
# for i in l1:
#     print(i, end=" ")
# l = [int(x) for x in input().split()]
# l1 = []
# for i,v in enumerate(l):
#     a = l.count(v)
#     if a>=2:
#         if not v in l1:
#             l1.append(v)
#
#
# l1.sort()
# for i in l1:
#     print(i, end=" ")

# def f(x):
#     # if  -2<x<=2:
#     #     return  -x/2
#     # elif x <=2 :
#     #     return 1-(x+2)**2
#     # elif 2<x:
#     #     return (x-2)**2 + 1

# def modify_list(l):
#     i=0
#     count=0
#     while True:
#         count+=1
#         if len(l)==0 or count==len(l):
#             break
#         if l[i]%2!=0 or l[i] ==0:
#             l.remove(l[i])
#             continue
#
#         l[i]//=2
#         i+=1
# def modify_list(l):
#     l1 = []
#     for i in l:
#         if i%2!=0 :
#             continue
#         l1.append(i)
#     for i in range(len(l1)):
#         l1[i]//=2
#     l.clear()
#     for i in l1:
#         l.append(i)
#
# lst = [1, 2, 3, 4, 5, 6]
# modify_list(lst)
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# for i in range(len(s)):
#     if s[i]==s[i+1]:
#         continue
#     l.append(s[i])
# print(l)


# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2*key in d:
#         d[key * 2] += [value]
#     else:
#         d[key*2] = [value]
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

# l = list(input().lower().split())
# d = {}
# for i in range(len(l)):
#     if l[i] not in d:
#         d[l[i]] = l.count(l[i])
# for key, val in d.items():
#     print(f"{key} {val}")

# d = {}
# for i in range(int(input())):
#     d.
#     print(f(int(input())))
# fin = open("C:\\Users\\User\\Desktop\\input1.txt", 'r')
# s = fin.readline().strip()
# l = s.split("")
# fin.close()
#
# fout = open("C:\\Users\\User\\Desktop\\output1.txt", 'r')
# for i in range(0,len(l),2):
#     fout.write(l[i]*int(l[i+1]))
# fout.close()
import requests
r = requests.get("https://vk.com/im?sel=c58")
print(r.text)
url = "https://music.yandex.ru/users/makarov21A/playlists"
par = {"key1":"val1", "key2":"val2"}
r = requests.get(url,params=par)
print(r.url)
b = arr


