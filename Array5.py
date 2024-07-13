n=int(input('n='))
listFib=[]
f1=1
f2=1
listFib.append(f1)
listFib.append(f2)
for i in range(2,n+1):
    f=f1+f2
    listFib.append(f)
    f1=f2
    f2=f
t=tuple(listFib)
print(t)