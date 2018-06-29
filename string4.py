a = 'something'+60*'-'+'DigitalLync'+50*'*'+'something'
print(a)
b = a.rstrip('*')
print(b)
c = b.lstrip('-')
print(c)
d = c.strip('something')
print(d)