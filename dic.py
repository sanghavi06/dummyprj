a={1:'hello','hi':45.78,34.76:2+9j}
#access the values form dic
print(a[1],a['hi'],a[34.76])
print(a)
a[1]='iam changed'
print(a)

a['key']='values'
print(a)
del a['key']
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a)
a.clear()
print(a)
a=['key1','key2','key3']
dic=dict.fromkeys(a)
print(dic)
d={a:a**3 for a in range(0,11)}
print(d)
print(len(d))
print(min(d))
print(max(d))
