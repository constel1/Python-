line = [1,7,6,11,3]
img = [[1,7,6,11,3], [1,7,6,11,3], [1,7,6,11,3], [1,7,6,11,3], [1,7,6,11,3]]
print(img)
img = [line[:], line[:], line[:], line[:], line[:]]
print(img)
print(img[3])
print(img[2][1])
img[1] = [0,0,0,0,0]
print(img)
img[1] = [0]*5
print(img)
img[1][2:] = [1] *5
print(img)
img[2][:] = [4]*6
print(img)
img.append("hdfjhdcfj")
print(img)
del img[0]
print(img)
print(img[4])
a = [[[True, False],[1,2,3]], ["матрица", "вектор"]]
print(a[0])#true...
print(a[0][0][1])













