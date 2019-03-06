import os, shutil
import fileinput
import re
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

logging.info('Start finding the latest build')
#find the latest build
AppMUPath=r'\\xxx\Build40\AppMU'
os.chdir(AppMUPath)
all_subdirs=os.listdir(AppMUPath)

for x in all_subdirs:
    latest_subdir = max(all_subdirs, key=os.path.getmtime)

    n=all_subdirs.index(latest_subdir)
    if not os.path.exists(os.path.join(latest_subdir,'Build.Completed.txt')):
        all_subdirs.pop(n)
    # recaculate the latest build folder
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    logging.debug('The updated build is '+ latest_subdir)
    
    buildpath=os.path.abspath(latest_subdir)
    logging.debug(buildpath)
##    print(latest_subdir)

###Search and replace the build number in arg file
### -define:BuildNumber_rainMain=latest_subdir
##os.chdir(r'C:\Depots\MBSI\Projects\AX\7.x\UI')
##
##f=['AX7.x_UI_BI.arg']
###update build number in AX7.x_UI_BI.arg
##fp = fileinput.input(files=f, inplace=True, backup='.bak')
##r= re.compile(r"BuildNumber_rainMain=.*", re.IGNORECASE)
##for line in fp:
##    print r.sub(r'BuildNumber_rainMain='+latest_subdir,line)
##fp.close()

###update buid path
##fp = fileinput.input(files=f, inplace=True, backup='.bak')
##r2 = re.compile(r'BuildRootPath_rainMain=.*',re.IGNORECASE)
##for line in fp:
##    print r2.sub(r'BuildRootPath_rainMain='+AppMUPath,line)
##fp.close()
def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

#copy the new/update files from \\xxx\Build40\AppMU\8.1.163.0\Retail\IPED\LCT\ar\file.txt.lct to a temp folder
#langs =["ar", "ar-AE", "cs", "da", "de", "de-AT", "de-CH", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-ZA", "es", "es-MX", "et", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "hu", "is", "it", "it-CH", "ja", "lt", "lv", "nb-NO", "nl", "nl-BE", "pl", "pt-BR", "ru", "sv", "th", "tr", "zh-Hans", ]
langs =["ar"]
for l in langs:
    localbuildpath=os.path.join('C:\\test\\'+latest_subdir+'\\'+l+'\\')
    if not os.path.exists(localbuildpath):
        os.makedirs(localbuildpath)
    Flist=open('C:\\Python27\\AXAppMUDailybuildcheck_updateFileNames.txt')
    Fobject=Flist.readlines()
    for p in Fobject:
        p=p.strip()      
        buildfilepath=os.path.join(buildpath+'\\Retail\\IPED\\LCT\\'+l+'\\'+p+".LCT")
        logging.info('Build file path is %s' % buildfilepath)
        
        localfilepath=os.path.join(localbuildpath+p+".LCT")
        if os.path.exists(buildfilepath):
            shutil.copy2(buildfilepath,localfilepath)
            logging.info('Copy to as local   %s' % localfilepath)
        else:
            logging.error('File doesn\'t exist in build %s' % buildfilepath)
            

