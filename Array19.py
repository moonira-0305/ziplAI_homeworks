import random as r
n=int(input('n='))
k=int(input('k='))
l=int(input('l='))
ArifMioyna=0
miqdor=0
mySet={20,90}
for i in range(2,n+1):
    mySet.add(r.randint(1,100))
print('Hamai elementho:',mySet)
myList=list(mySet)
newList=myList[k:l]
for i in newList:
    ArifMioyna+=i
    miqdor+=1
print('Miyonai arifmetiki ',ArifMioyna/miqdor)




