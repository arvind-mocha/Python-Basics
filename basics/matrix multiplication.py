from numpy import *

# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[input("enter you first matrix")],
    [input()],
    [input()]]
# 3x4 matrix
Y = [[input("enter your second matrix")],
    [input()],
    [input()]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)