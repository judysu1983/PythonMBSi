import os
#copy all the target resjson to C:\test\mobile-app for process

os.chdir('C:\\test\\mobile-app\\ts')
tsfiles=os.listdir('.')
os.chdir('C:\\test\\mobile-app\\resjson')
resjsonFiles=os.listdir('.')
i=0
for resjson in resjsonFiles:

    ts=tsfiles[i]
    print(i)
    print(resjson)
    print(ts)
    f=open(resjson).readlines()
    #remove first and last line, {}
    open(ts,'w').writelines(f[1:-1])
    fts=open(ts,'a')
    #append last line as };
    fts.write('};')
    fts.close()
    fts=open(ts,'r')
    contents=fts.readlines()
    fts.close()
    #insert to first and second lines
    contents.insert(0,"/* tslint:disable */\n")
    contents.insert(1,"export var messages = {\n")
    fts=open(ts,'w')
    contents=''.join(contents)
    fts.write(contents)
    fts.close()
    i=i+1
    
    
    
