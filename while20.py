n=int(input('n='))
k=n
while k!=0 and n!=2:
    n=k%10
    k=k//10
print(n==2)

