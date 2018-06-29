a = ((4,5),(2,7))

b = ((3,2),(9,1))

result = ((0,0),(0,0))
for i in range(len(a)):
  for j in range(len(a[0])):

    result(i)(j) = a(i)(j) + b(i)(j)
for r in result :
  print(r)



#a = [[4,5,6],[2,7,6],[3,5,6]]

#b = [[3,2,6],[9,1,8],[3,9,1]]

#c = [[4,7,9],[5,8,2],[7,4,2]]

#result = [[0,0,0],[0,0,0],[0,0,0]]

#for i in range(len(a)):
 # for j in range(len(b)):

  	
 #   result[i][j]=a[i][j]+b[i][j]+c[i][j]
#for r in result :
  #print(r)
#m=[1,2,3,4]
#n=[6,8,4,9]
#result=[0,0,0,0]
#for i in range(len(m)):
#  for j in range(len(n)):
 # 	result[i][j]=m[i]+n[j]
#for r in result:
#  print(r)
