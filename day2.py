 #
#
# b = [[1,2,3], [4,5,6], [7,8,9]]
# print(b)
# a = [ x
#      for row in b
#      for x in row
#      ]
# print(a)
# M, N = 3,4
# matrix = [[a for a in range(M)] for j in range(N)]
# print(matrix)
# A = [[1,2,3], [4,5,6], [7,8,9]]
# print(A)
# A = [[a**2 for a in row] for row in A]
# print(A)
# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# A = [[row[i] for row in A] for i in range(len(A[0]))]
# print(A)
g = [u **2 for u in [x+1 for x in range(5)]]
print(g)





