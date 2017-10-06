import xml.etree.ElementTree as ET
import os, shutil,stat

#Copy files from sd to git folder structure by C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol:
#e.g. from C:\Depots\MBSI\Projects\OOB\UI\Master\source\HCMApp\Calendars.en-US.label.txt
#     to C:\SourceMonitor\SDCopy\f\en-US\
#f= Accounting Foundation\source\metadata\Calendar\Calendar\AxLabelFile\LabelResources
SDCopy=r'C:\SourceMonitor\SDCopy'
HCMsdPath=r'C:\Depots\MBSI\Projects\OOB\UI\Master\source\HCMApp'
root = ET.parse(r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol').getroot()
files = root.findall("./Project/Component/ItemGroup/File")

def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

#remove all the files under C:\SourceMonitor\SDCopy    
if os.path.exists(SDCopy):
    shutil.rmtree(SDCopy, onerror=del_rw)
os.makedirs(SDCopy)

for f in files:

    sdfile=os.path.join(HCMsdPath,f.get('name'))
    print('From ' +sdfile)
    targetfile=os.path.join(SDCopy, f.getchildren()[3].text,'en-US',f.get('name'))
    print('To ' +targetfile)
    print('')
    if not os.path.exists(os.path.join(SDCopy, f.getchildren()[3].text,'en-US')):
        os.makedirs(os.path.join(SDCopy, f.getchildren()[3].text,'en-US'))
    if os.path.exists(sdfile):
        if not os.path.exists(targetfile):
            shutil.copy2(sdfile,targetfile)
    
