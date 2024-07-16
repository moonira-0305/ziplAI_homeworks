#case4
moh=int(input('raqami tartibii mohro dohil kuned'))
ruzhoiMohDict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:32,9:30,10:31,11:30,12:31}
if moh in ruzhoiMohDict.keys():
    print('Dar mohi ',moh,'-um ',ruzhoiMohDict[moh],'ruz hast')
else:
    print('in hel moh nest!')