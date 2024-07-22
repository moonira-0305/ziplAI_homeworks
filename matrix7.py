import random as r
m=int(input('m='))
n=int(input('n='))
k=int(input('k='))
matrix=[]
for i in range(m):
    satr=[]
    for j in range(n):
        qimat=r.randint(1,100)
        satr.append(qimat)
    matrix.append(satr)
print('Matritsa:')
for row in matrix:
    print(" ".join(map(str, row)))

print('satri ',k,'-um:')
for j in range(n):
    print(matrix[k-1][j], end=' ')
