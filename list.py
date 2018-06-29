#l = [1,2,3,'hello',45.8,67+9j]
#print(l)
#print(type(l))
#print(type(l[0]),type(l[3]))

#a = []
#print (type(a))

l1 = [1,2,3,'hello',45.8,67+9j]
l2 = [4,5,6,7]
c = l1+l2
print(c)
#del c[1]
#print(c)
c.pop()
print(c)
c.pop()
print(c)
l1.append(2)
print(l1)
l1.insert(3,l2)
print(l1)