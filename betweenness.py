A = [[0,0,0,0,0,0,1],
     [0,0,0,0,0,0,1],
     [0,0,0,1,1,0,1],
     [0,0,1,0,1,0,0],
     [0,0,1,1,0,1,1],
     [0,0,0,0,1,0,0],
     [1,1,1,0,1,0,0]]

D = [-1 for i in range(len(A))]
D[0] = 0

Q = []
Q.append(0)

W = [0 for i in range(len(A))]
W[0] = 1

i = 0
d = 0
while True:
    if not -1 in D:
        break

    for j in range(len(A)):
        if A[i][j] == 1:
            if D[j] == -1:
                D[j] = d + 1
                W[j] = W[i]
                Q.append(j)
            if not D[j] == -1 and D[j] == d + 1:
                W[j] = W [j] + W[i]
            if not D[j] == -1 and D[j] < d + 1:
                continue
    d += 1
    i += 1

print(D)
print(Q)
print(W)