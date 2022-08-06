# adjacency matrix
A = [[0,0,0,0,0,0,1],
     [0,0,0,0,0,0,1],
     [0,0,0,1,1,0,1],
     [0,0,1,0,1,0,0],
     [0,0,1,1,0,1,1],
     [0,0,0,0,1,0,0],
     [1,1,1,0,1,0,0]]

# degree of nodes
K = []

# numerator
numberOfTriangel = 0.

# denuminator
numberOfConnectedPath = 0.

for i in range(len(A)):
    for m in range(i+1):
        for n in range(i+1):
            if A[i][m] == 1 and A[i][n] == 1 and A[m][n] == 1:
                numberOfTriangel += 1
    K.append(sum(A[i]))

for i in range(len(A)):
    numberOfConnectedPath += K[i] * (K[i] - 1)

numberOfTriangel *= 0.5
numberOfConnectedPath *= 0.5

print((numberOfTriangel*3)/numberOfConnectedPath)