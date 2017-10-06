tsfile='C:\\SourceMonitor\\GitCopy\\mobile-app\\src\\localization\\messages\\en-us.ts'
resjsonfile='C:\\SourceMonitor\\GitCopy\\mobile-app\\src\\localization\\messages\\en-us.resjson'
#C:\SourceMonitor\GitCopy\mobile-app\src\localization\messages\en-us.ts
f=open(tsfile).readlines()
#remove line 1,2 and the last line of f and write lines to resjson
open(resjsonfile,'w').writelines(f[2:-1])
f2=open(resjsonfile,'a')
f2.write('}')
f2.close()

f2=open(resjsonfile,'r')
contents=f2.readlines()
f2.close()

#insert { as the fisrt line
contents.insert(0,"{\n")
f2=open(resjsonfile,'w')
contents=''.join(contents)
f2.write(contents)
f2.close()

