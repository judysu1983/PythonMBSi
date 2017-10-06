import xml.etree.ElementTree as ET
import os, shutil

#Copy file from sd to git folder structure:
#e.g. from C:\Depots\MBSI\Projects\OOB\UI\Master\source\HCMApp\Calendars.en-US.label.txt
#f= Accounting Foundation\source\metadata\Calendar\Calendar\AxLabelFile\LabelResources

#C:\SourceMonitor\SDCopy\f\en-US\
SDCopy=r'C:\SourceMonitor\SDCopy'
sdPath=r'C:\Depots\MBSI\Projects\OOB\UI\Master\source\HCMApp'
root = ET.parse(r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol').getroot()
files = root.findall("./Project/Component/ItemGroup/File")



for f in files:
    #print(f.get('name'))
    targetfile=os.path.join(SDCopy, f.getchildren()[3].text,'en-US',f.get('name'))
    print(targetfile)
    sdfile=os.path.join(sdPath,f.get('name'))
    print(sdfile)
    if not os.path.exists(os.path.join(SDCopy, f.getchildren()[3].text,'en-US')):
        os.makedirs(os.path.join(SDCopy, f.getchildren()[3].text,'en-US'))
    if os.path.exists(sdfile):
        shutil.copy2(sdfile,targetfile)
    
