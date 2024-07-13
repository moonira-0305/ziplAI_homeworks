n=int(input('n='))
myList=[]
for i in range(0,n+1):
    myList.append(i*2)
t=tuple(myList)
print(t[::-1])
