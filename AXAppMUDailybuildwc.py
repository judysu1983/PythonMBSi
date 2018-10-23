import os
import fileinput
import re

#find the latest build
AppMUPath=r'\\dcsrdbldcfsb\Build40\AppMU'
os.chdir(AppMUPath)
all_subdirs=os.listdir(AppMUPath)
##for x in all_subdirs:
##    print x.startswith('8')
##if any(x.startswith('8.0') for x in all_subdirs):
##    all_subdirs.pop()
##           all_subdirs.pop(x)
print all_subdirs

for x in all_subdirs:
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    print(latest_subdir)
    n=all_subdirs.index(latest_subdir)
    if not os.path.exists(os.path.join(latest_subdir,'Build.Completed.txt')):
        all_subdirs.pop(n)
    # recaculate the latest build folder
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    print(all_subdirs)
    print('updated '+ latest_subdir)
    
    print(os.path.abspath(latest_subdir))
##    print(latest_subdir)

#search and replace the build number in arg file
# -define:BuildNumber_rainMain=latest_subdir
os.chdir(r'C:\Depots\MBSI\Projects\AX\7.x\UI')

f=['AX7.x_UI_BI.arg']
#update build number in AX7.x_UI_BI.arg
fp = fileinput.input(files=f, inplace=True, backup='.bak')
r= re.compile(r"BuildNumber_rainMain=.*", re.IGNORECASE)
for line in fp:
    print r.sub(r'BuildNumber_rainMain='+latest_subdir,line)
fp.close()

###update buid path
##fp = fileinput.input(files=f, inplace=True, backup='.bak')
##r2 = re.compile(r'BuildRootPath_rainMain=.*',re.IGNORECASE)
##for line in fp:
##    print r2.sub(r'BuildRootPath_rainMain='+AppMUPath,line)
##fp.close()


#copy the new/update files from \\dcsrdbldcfsb\Build40\AppMU\8.1.163.0\Retail\IPED\LCT to a temp folder


