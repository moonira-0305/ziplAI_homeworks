n=int(input('n='))
a=int(input('a='))
d=int(input('d='))
myList=[]
for i in range(0,n+1):
    myList.append(a*d**i)
print(myList)