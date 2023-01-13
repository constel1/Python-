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
s = input()
l = []
for i in range(len(s)):
    if s[i]==s[i+1]:
        continue
    l.append(s[i])
print(l)
