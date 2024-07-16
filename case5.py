#case5
n=int(input('raqami tartibii amalro dohil kuned'))
a=float(input('a='))
b=float(input('b='))
myDict={1:a+b,2:a-b,3:a*b,4:a/b}
if n in myDict.keys():
    print('amali',n,'-um intihob shud, qimat: ',myDict[n])
else:
    print('in hel amal nest!')
