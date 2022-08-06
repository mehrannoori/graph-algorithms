#from collections import defaultdict

# adjacency matrix
A = [[0,0,0,0,0,0,1],
     [0,0,0,0,0,0,1],
     [0,0,0,1,1,0,1],
     [0,0,1,0,1,0,0],
     [0,0,1,1,0,1,1],
     [0,0,0,0,1,0,0],
     [1,1,1,0,1,0,0]]

#path = defaultdict(list)


d = 0
D = [-1 for i in range(len(A))]
D[4] = 0

Q = []
Q.append(4)

i = 0

while True:
     if not -1 in D:
          break

     d = D[Q[i]]
     for j in range(len(A)):
          if A[Q[i]][j] == 1 and D[j] == -1:
               D[j] = d+1
               Q.append(j)
               #path[Q[i]].append(j)
     i += 1

print(D)
print(Q)
#print(path)