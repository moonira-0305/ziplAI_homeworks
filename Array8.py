import random as r
n=int(input('n='))
miqdor=0
mySet={20,90}
for i in range(2,n+1):
    mySet.add(r.randint(1,100))
print('Hamai elementho:',mySet)
print('Toqho: ',end=' ')
for i in mySet:
    if i%2==1:
        print(i,end=' ')
        miqdor+=1
print('Miqdori toqho:',miqdor)
