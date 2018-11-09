import os, shutil
import fileinput
import re,sys
import logging
os.chdir(r'C:\Python27')
os.remove('AppMUStablog.txt')
logging.basicConfig(filename='AppMUStablog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
##logging.disable(logging.DEBUG)
#############
#####Sanity check on lct files from builds and custom 3 values in each langauge#############
logging.info('Start finding the latest build')
#find the latest build
AppMUPath=r'\\dcsrdbldcfsb\Build41\AppMUStab'
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

def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

#copy the new/update files from \\dcsrdbldcfsb\Build40\AppMU\8.1.163.0\Retail\IPED\LCT\ar\file.txt.lct to a temp folder
langs =["ar", "ar-AE", "cs", "da", "de", "de-AT", "de-CH", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-ZA", "es", "es-MX", "et", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "hu", "is", "it", "it-CH", "ja", "lt", "lv", "nb-NO", "nl", "nl-BE", "pl", "pt-BR", "ru", "sv", "th", "tr", "zh-Hans", ]
#langs =["ar"]
for l in langs:
    localbuildpath=os.path.join('C:\\test\\'+latest_subdir+'\\'+l+'\\')
    if not os.path.exists(localbuildpath):
        os.makedirs(localbuildpath)
    Flist=open('C:\\Python27\\AXAppMUStabDailybuildcheck_updateFileNames.txt')
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

logging.debug('===========The updated build is '+ latest_subdir)
#update the search path in SearchbyCustom3.srs           
os.chdir(r'C:\Python27\SRscript')
f=['SearchbyCustom3.srs']
fp = fileinput.input(files=f, inplace=True, backup='.bak')
r= re.compile(r"AppMUStab\\[0-9\.]+", re.IGNORECASE)
for line in fp:
    print r.sub(r"AppMUStab\\"+latest_subdir,line)
fp.close()
os.system(r"C:\Users\v-judysu\Downloads\SR\SR32.exe /cC:\Python27\SRscript\RemoveemptyLines.srs /r /n /q")

##############################update Search*srs for the updated custom 3 value.
# search and replace to reformat the result
os.system(r"C:\Users\v-judysu\Downloads\SR\SR32.exe /cC:\Python27\SRscript\SearchbyCustom3.srs /s /n /q")
os.system(r"C:\Users\v-judysu\Downloads\SR\SR32.exe /cC:\Python27\SRscript\reformateResults.srs /r /n /q")
shutil.copy2(r'C:\Python27\SRscript\searchbyC3results.txt', os.path.join(r'C:\Python27\SRscript\\'+latest_subdir+'.log'))
shutil.copy2(r'C:\Python27\AppMUStablog.txt', os.path.join(r'C:\Python27\SRscript\\'+latest_subdir+'AppMUStabcopy.log'))



