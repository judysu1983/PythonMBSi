#https://www.youtube.com/watch?v=rFxXDO8-keg&t=207s
import os

from xml.etree import ElementTree
os.chdir(r'C:\Gitprojects\HCM')

for floderName, subfolders,filenames in os.walk(r'C:\Gitprojects\HCM'):
    for f in filenames:
        if f.endswith('en-US.xml'):
            file_name,file_ext=os.path.splitext(f)
            f_basename,f_other=file_name.split('_')
            print(f_basename)
    
##file_name="Payroll_en-US.xml"
##full_file = os.path.abspath(file_name)
##
##dom= ElementTree.parse(full_file)
##names= dom.findall('RelativeUriInModelStore')
##for c in names:
##    print(c.text)
