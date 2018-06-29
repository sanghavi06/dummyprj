a = {1,'hello',(45,34,62),45+7j}
print(a)
print(type(a))
#a.update([1,2,3,4])
#a.add(6)
#a.append(5)
#a.insert(9)
a={i for i in range(0,10,2)}
print(a)
b={i for i in range(0,10,3)}
print(b)
#print(a+b)
#print(a-b)
#print(a.difference(b))
#print(b.difference(a))
#print(a.symmetric_difference(b))
#print(b.symmetric_difference(a))
#a.pop()
#print(a)
#a.clear()
#print(a)
#print(a|b)
#print(a.union(b))
print(a&b)
print(a.intersection(b))
#a={1,2,3,4,5,6,7,8}
#b={1,2,3}
#print(a.issubset(b))
#print(a.issuperset(b))
a={i for i in range(0,11)}
print(a)
fset = frozenset(a)
print(fset)
