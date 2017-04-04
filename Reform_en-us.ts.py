tsfile=C:\\SourceMonitor\\Git\\D365App\\UI\\Master\\Source\\mobile-app\\en-us.ts
f=open(tsfile).readlines()
open('new.resjson','w').writelines(f[2:-1])
f2=open('new.resjson','a')
f2.write('}')
f2.close()

f2=open('new.resjson','r')
contents=f2.readlines()
f2.close()

contents.insert(0,"{\n")
f2=open('new.resjson','w')
contents=''.join(contents)
f2.write(contents)
f2.close()

