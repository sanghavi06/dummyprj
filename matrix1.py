m=int(input("enter number of row"))
n=int(input("enter number of column"))
Mat=[]
for i in range(0,m):
	Mat.append([])
for i in range(0,m):
	for j in range(0,n):
		Mat[i].append(j)
		Mat[i][j]=0
for i in range(0,m):
  for j in range(0,n):
  	print('entry in row:',i+1,'column:',j+1)
  	Mat[i][j]=int(input())
  	print(Mat)

result = [[0,0],[0,0]
for i in range(len(m)):
	for j in range(len(n)):

      result[i][j] = m[i][j] + n[i][j]
for r in result :
    print(r)
