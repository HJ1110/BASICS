L = [10, 20, [22, 23, 24], [45, 56, 78]]
print(L[2][1])

print(len(L))

print(len(L[2]))

print("school")

print(list("school"))

print(L.index(20))

p = [90, 100, 110]
L.extend(p)
print(L)

L.insert(3, 999)
print(L)

L.insert(len(L), -123)
print(L)

p.insert(-2, 999)
print(p)

L.pop(1)
print(L)

L.pop()
print(L)

L.remove(999)
print(L)

L.clear()
print(L)

L = [10, 29, 20, 10, 10, 29]
print(L.count(10))
L.reverse()
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

print(min(L), max(L), sum(L))

L[0] = 1000
print(L)

del L[2]
print(L)

del L[0:2]
print(L)

a = (2, 4, 6, 5, 8)
b = (34, 45, 56)
for i in a:
    print(i)

print(len(a))
for i in range(0, len(a)):
    print(a[i])

print(a[::-1])

print(a == b)
x, y, z, w, r = a
print(x, y, z, w, r)

t = tuple()
print(t)
print(type(t))
l=[]
print(type(l))
x = "school"
print(type(x))

a = input("enter the first no.")
b = int(input("enter the second no."))
a = a+"1"
print(a)
b = b+1
print(b)

t = tuple()
n = int(input("how many elements"))
for i in range(n):
    a = input("enter the no.")
    t = t+(a,)
print((t))
p = (2,4,5)
l = t+p
print(l)
for i in t:
    print(i)
for i in range(n):
    print(t[i])
print(t[::-1])
print(t[-3:-1]+(t[0],))
print(t*2)
g = (input("enter the value"))
print(g not in t)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(len(a))
print(a.count(2))
l = sorted(a)
print(a)
print(l)

a = (45, 45, 1, 2, 3, 4, 5, 6, 78)
print(len(a))
print(a.count(2))
l = sorted(a)
print(a)
print(l)
print(a.index(45), 3)

dict = {"name": "ram", "age":7, "class": "XI"}
print(dict)
print(type(dict))
for i in dict:
    print(i, ":", dict[i])

d1 = {"mon": "monday", "tue": "tuesday", "wed": "wednesday"}
d1["thu"] = "thursday"
print(d1)
d1["fri"] = "friday"
print(d1)
d1["fri"] = "FRIDAY"
print(d1)
d2 = {"sat": "saturday"}
print(d2)
d1.update(d2)
print(d1)
del d1["sat"]
print(d1)
d1.pop("fri")
print(d1)
print("thu" in d1)
print(len(d1))
print(d1.items)
print(d1.keys())
print(d1.values())

stu = dict
i = 1
n=int(input("how many entry"))
while i<=n:
    adm = input("admission no")
    nm = input("name")
    sec = input("section")
    per = float(input("enter %"))
    b = (nm, sec, per)
    stu[adm] = b
    i = i+1
l = stu.keys()

for i in l:
    print("admission no", i, ":")
    z = stu[i]
    for j in z:
        print(j, end= " ")
print(stu)
