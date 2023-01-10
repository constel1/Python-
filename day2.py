import math
# M, N, B = list(map(int, input().split()))
# a = [[0 for i in range(N)] for row in range(M)]
#
# for i in range(B):
#     x,y=list(map(int, input(f"Введите координаты бомбы номер {i+1}\n").split()))
#
#     a[int(x-1)][int(y-1)] = -1
#
# for i in range(M):
#     for j in range(N):
#         if a[i][j] == 0:
#             for i1 in range(-1,2):
#                 for j1 in range(-1, 2):
#                     ai = i + i1
#                     aj = j + j1
#                     # (ai, aj)
#
#                     if 0 <= ai < M and 0 <= aj < N and a[ai][aj] == -1:
#                         a[i][j] += 1
#
#
#
#
#
# for i in range(M):
#     for j in range(N):
#         if a[i][j] == -1:
#             print('*', end='\t')
#         elif a[i][j] == 0:
#             print('.', end='\t')
#         else:
#             print(a[i][j], end='\t')
#     print()

# b =a[0]
# for i in a:
#     if b>i:
#         b = i
# print(f"b = {b}")
# d = []
# sum = 0
# while True:
#     a = int(input("число: "))
#     d.append(a)
#     sum+=d[-1]
#
#     if sum==0:
#         break
#
# a = [x**2 for x in d]
# for i in a:
#     sum+=i
# print(sum)
# a1 = int(input())
# s= a1
# s2 = 0+abs(a1**2)
# while s!=0:
#     a1 = int(input())
#     s = s + a1
#     s2 = s2+abs(a1)**2
#     if s==0:
#         break
# print(s2)
#
# a = list(map(int, input().split()))
# b = int(input())
# for i,k in enumerate(a):
#     if k == b:
#         print(i, end=" ")
# if a.count(b)==0:
#     print("Отсутствует")
# ind = [i  for i in range(0,len(a)) if a[i] ==b] if a.count(b)!=0 else "Отсутствует"
# print(ind)
# print(9**19 - int(float(9**19)))
# x,h,m = int(input()),int(input()),int(input())
# print(((h*60)+m+x)//60)
# print(((h*60)+m+x)%60)
# a,b,h = int(input()),int(input()),int(input())
# if h<a:
#     print("Недосып")
# elif a<=h<=b:
#     print("Это нормально")
# else:
#     print("Пересып")

# a = int(input())
# if a%4==0 and a%100!=0 or a%400 ==0:
#     print("Високосный")
# else:
#     print("Обычный")
# print("123" + "42")

# a, b, c = int(input()), int(input()), int(input())
# p = (a+b+c)/2
# s =math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(s)
# a,b,oper =float(input()),float(input()),input()
# if oper == "+":
#     print(a+b)
# elif oper == "-":
#     print(a-b)
# elif oper == "*":
#     print(a*b)
# elif oper == "/":
#     if b==0:
#         print("Деление на 0!")
#     else:
#         print(a/b)
# elif oper == "pow":
#     print(a**b)
# elif oper == "div":
#     print(a//b)
# elif oper == "mod":
#     if b == 0.0:
#         print("Деление на 0!")
#     else:
#         print(a % b)

# f = input()
# if f == "треугольник":
#     a,b,c = float(input()),float(input()),float(input())
#     p = (a + b + c) / 2
#     s =math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print(s)
# elif f == "прямоугольник":
#     a, b = float(input()), float(input())
#     print(a*b)
# elif f == "круг":
#     print(3.14 * (float(input())**2))
# else:
#     print("Неправильнный ввод!")
# a,b,c = int(input()),int(input()),int(input())
# if max(a,b,c)==a:
#     print(a)
#     if min(b,c) == b:
#         print(b)
#         print(c)
#     else:
#         print(c)
#         print(b)
# elif max(a,b,c)==b:
#     print(b)
#     if min(a,c) == a:
#         print(a)
#         print(c)
#     else:
#         print(c)
#         print(a)
# elif max(a,b,c)==c:
#     print(c)
#     if min(a,b) == a:
#         print(a)
#         print(b)
#     else:
#         print(b)
#         print(a)
# while True:
#     n = int(input())
#     if n <0:
#         break
# if 11<=n%100<=16 or n==0 or (n%100)%10==0:
#     print(f"{n} программистов")
#
# elif n%10 ==1:
#     print(f"{n} программист")
# elif 2<=n%10<=4 and 10<((n%100)//10)<20:
#      print(f"{n} программиста")
# elif 2<=n%10<=4:
#     print(f"{n} программиста")
# else:
#     print(f"{n} программистов")
a = list(map(int," ".join(input()).split()))
print(a)
if sum(a[:3])==sum(a[3:]):
    print("Счастливый")
else:
    print("Обычный")

