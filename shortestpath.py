class Node:
    def __init__(self, i, p=None):
        self.index = i
        self.prev = p
        self.distance = -1

A = [[0,0,0,0,0,0,1],
     [0,0,0,0,0,0,1],
     [0,0,0,1,1,0,1],
     [0,0,1,0,1,0,0],
     [0,0,1,1,0,1,1],
     [0,0,0,0,1,0,0],
     [1,1,1,0,1,0,0]]

R = range(len(A))

D = [Node(i) for i in R]
D[0].distance = 0

Q = []
Q.append(Node(0))

i = 0
t = 5

while True:
    if not D[t].distance == -1:
        break

    d = D[Q[i].index].distance
    for j in R:
        if A[Q[i].index][j] == 1 and D[j].distance == -1:
            D[j].distance = d+1
            Q.append(Node(j,Q[i]))
                      
    i += 1

final = None
for i in range(len(Q)):
    if Q[i].index == t:
        final = Q[i]

print(final.index)
while True:
    if final.prev == None: break
    else:
        print(final.index)
        final = final.prev