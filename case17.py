n=int(input('adad?'))
a1=n//10
a2=n%10
dahDict={1:'ёздаҳ',2:'дувоздаҳ',3:'сенздаҳ',4:'чордаҳ',5:'понздаҳ',6:'шонздаҳ',7:'ҳабдаҳ',8:'ҳаждаҳ',9:'нуздаҳ'}
raqamiYakumDict={2:'бист',3:'си',4:'чил',5:'панҷоҳ',6:'шаст',7:'ҳафтод',8:'ҳаштод',9:'навад'}
raqamiDuyumDict={1:'у як',2:'у ду',3:'у се',4:'у чор',5:'у панҷ',6:'у шаш',7:'у ҳафт',8:'у ҳашт',9:'у нӯҳ'}
if a1 in raqamiYakumDict.keys():
    print(raqamiYakumDict[a1],end='')
if a2 in raqamiDuyumDict.keys() and a1!=1:
    print(raqamiDuyumDict[a2],end=' ')
elif a1==1:
    if a2 in dahDict.keys():
        print(dahDict[a2], end=' ')
print(' масъала')