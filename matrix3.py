r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
Mat=[ ]

for i in range(r):
    Mat.append([ ])
    for j in range(c):
        x=int(input("Enter the element"))
        Mat[i].append(x)

    print(Mat)﻿