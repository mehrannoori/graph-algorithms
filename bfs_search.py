# adjacency matrix
A = [[0,0,0,0,0,0,1],
     [0,0,0,0,0,0,1],
     [0,0,0,1,1,0,1],
     [0,0,1,0,1,0,0],
     [0,0,1,1,0,1,1],
     [0,0,0,0,1,0,0],
     [1,1,1,0,1,0,0]]

d = 0
D = [-1 for i in range(len(A))]
D[0] = 0

while True:
    if -1 not in D:
        break

    for i in range(len(D)):
        if D[i] == d:
            for j in range(len(A)):
                if A[i][j] == 1 and D[j] == -1:
                    D[j] = d+1
            
    d += 1

print(D)