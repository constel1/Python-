


a= [1,2,3]

c = a[:]
print(c)
c*=2
print(c)
print("her" in c)
del c[3]

a = c
print(f"\tid c{id(c)}\n", c)
print(f"\tid c{id(a)}\n", a)

print(a)
print(c)
print("werty"[1::2])
print(sorted(c, reverse=True))
print(c[::-1])
c[2:4] = "хорошо", "отлично"
print(c)
c[2:4] = 10,20
print(c)