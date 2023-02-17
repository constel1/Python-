
# mass=[
# [1,0],
# [2,1],
# [3,2],
# [4,6],
# [5,0],
# [6,0],
# [7,2]
# ]
# protection=[0,0,0,0,0,0,0]
# def printChild(parent,level):
#      for i in range(len(mass)):
#          if (mass[i][1]==parent):
#              if (mass[i][0] in protection):
#                 return
#              for j in range(level):
#                 print('-', end='')
#              print(mass[i][0], end='')
#              print()
#              # print(' ', protection)
#              protection[i]=mass[i][0]
#              printChild(mass[i][0],level+1)
#      return
# printChild(0,0)


# arr= ['H','E','L','L','O']
# key= [' ',' ',' ']
# lenA=len(arr)
# lenK=len(key)
# j=0
# for i in range(lenA):
#     if (j>=lenK):
#         j=0
#     arr[i]=chr(ord(arr[i])^ord(key[j]))
#     j=j+1
# for i in range(lenA):
#     print(ord(arr[i]),arr[i])
d = int(input())
n = 8
s = 78
while s <= 1200:
    s= s+d
    print(s)
    n = n+2
print()
print(n)
