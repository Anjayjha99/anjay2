l = ["Ferrari","Mercedes","Ducati","BMW"]
print(l)
print(l+l)
print(l*3)
l.append("Jaguar")
print(l)
l.insert(1,"Kiwi")
print(l)
l.pop(2)
print(l)
l.remove("Ducati")

for i in l:
    print(i)

if "BMW" in l:
    print("BMW is there")
c = ["abc", "def","ghi"]
l.extend(c)
print(l)
c.clear()
print(c)


