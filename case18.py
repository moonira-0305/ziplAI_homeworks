#case18
n=int(input('adad?'))
a1=n//100
a2=(n%100)//10
a3=n%10
dahDict={1:'ёздаҳ',2:'дувоздаҳ',3:'сенздаҳ',4:'чордаҳ',5:'понздаҳ',6:'шонздаҳ',7:'ҳабдаҳ',8:'ҳаждаҳ',9:'нуздаҳ'}
raqamiDuvumDict={2:'бист',3:'си',4:'чил',5:'панҷоҳ',6:'шаст',7:'ҳафтод',8:'ҳаштод',9:'навад'}
raqamiSevumDict={1:'як',2:'ду',3:'се',4:'чор',5:'панҷ',6:'шаш',7:'ҳафт',8:'ҳашт',9:'нӯҳ'}
if a1 in raqamiSevumDict.keys():
    print(raqamiSevumDict[a1],' сад',end='')
if a1!=0:
    print('у ',end='')
if a2 in raqamiDuvumDict.keys():
    print(raqamiDuvumDict[a2],end='')
if a2!=0 and a2!=1:
    print('у ',end='')
if a3 in raqamiSevumDict.keys() and a2!=1:
    print(raqamiSevumDict[a3],end=' ')
elif a2==1:
    if a3 in dahDict.keys():
        print(dahDict[a3])
