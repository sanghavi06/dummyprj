#t = 1,2,3,4,5
#print(t)
#a = (1,1,'hello',45.7,8+9j)
#b = (5,3,7,8)
#for i in a:
#	print(i,end=' ')
#print(a+b)
#print(2*a+2*b)
#del a[1]
#a.remove()
#b.pop()
#count=a.count(1)

#generator objects

#a=(i for i in range(0,11))
#print(a)
#for i in a:
	#print(i)
#print(next(a))
#print(next(a))


#enumerator objects
#a=('batman','ironman','superman')
#enum=enumerate(a)
#enum = list(enumerate(a))
#print(enum)
#print(next(enum))
#print(next(enum))
#for i in enum:
#	print(i)


#inbuilt function
#a = (0,1,3)
#print(all(a))
#print(any(a))
#print(max(a))
#print(min(a))
#print(enumerate(a))
#print(len(a))
#print(tuple(a))

l=[1,2,(45,67),78]
t=(2,3,4,[5,22,34],78)
#l[2][0]='am changed'
#print(l)
t[3][1]='am changed'
print(t)