i=1
s=0
N = int(input("До скольки подсчитать сумму? - "))
while i<20:
    if i%2!=0:
        s+=i
    i+=1
print(f"sum = {s}")

pass1 = "werty"
ps = ""
while True:
    ps = input("Input your password - ")
    if ps!= pass1:
        print("ERROR!")
        continue
    break
print("correct password ")
s = 0
i =-10
while i<100:
    if i==0:
        break
    s+=1/i
    i+=1
else:
    print("Сумма вычисленна корректно")
print(s)
d = [9,5,8,4,5]

print(d)
for i in range(len(d)):
    d[i] *= 2
print(d)