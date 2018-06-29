print("enter n for n*n matrix")
n=input()
matrix1 = []
matrix2 = []
add_matrix=[]
for i in range(0,n):
  a = []
  for j in range(0,n):
  	a.append(matrix1[i][j]+matrix2[i][j])
  add_matrix.append(a)
print("addition of matrix is",add_matrix)