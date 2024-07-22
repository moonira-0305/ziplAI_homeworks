import random as r
miqdor=0
mySet={20,90}
for i in range(2,11):
    mySet.add(r.randint(1,100))
print('Hamai elementho:',mySet)
last_element=list(mySet)[-1]
print('last_element=',last_element)
for x in mySet:
    if x<last_element:
        print('x=',x)
        break