import random as r
m=int(input('m='))
n=int(input('n='))
d=int(input('d='))
myListM=[]
for i in range(0,m):
    myListM.append(i+1)
matritsa=[]
for i in range(m):
    satr=[]
    for j in range(n):
        qimat=myListM[i]+j*d
        satr.append(qimat)
    matritsa.append(satr)

for row in matritsa:
    print(" ".join(map(str, row)))




