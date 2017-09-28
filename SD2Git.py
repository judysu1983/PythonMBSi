import xml.etree.ElementTree as ET
import os, shutil,stat

#Copy files from sd to git folder structure by C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol:
#e.g. from C:\Depots\MBSI\Projects\OOB\UI\Master\source\HCMApp\Calendars.en-US.label.txt
#     to C:\SourceMonitor\SDCopy\f\en-US\
#f= Accounting Foundation\source\metadata\Calendar\Calendar\AxLabelFile\LabelResources

SDCopy=r'C:\SourceMonitor\SDCopy'
def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

#remove all the files under C:\SourceMonitor\SDCopy    
if os.path.exists(SDCopy):
    shutil.rmtree(SDCopy, onerror=del_rw)
os.makedirs(SDCopy)

def sd2git(Master,Component,EOLfile):

    root = ET.parse(EOLfile).getroot()


    #".//ItemGroup/..[@name='PowerApps-CDM-Entities']"
    #xpathExpression=('.//ItemGroup/..[@name="%s"]' %Component)
    print('.//ItemGroup/..[@name="%s"]' %Component)
    coms=root.findall('.//ItemGroup/..[@name="%s"]' %Component)
    for c in coms:
        files=c.findall("./ItemGroup/File")
        for f in files:
            print(f.get('name'))

            sdfile=os.path.join(Master,Component,f.get('name'))
            print('From ' +sdfile)
            targetfile=os.path.join(SDCopy, f.getchildren()[3].text,'en-US',f.get('name'))
            print('To ' +targetfile)
            print('')
            if not os.path.exists(os.path.join(SDCopy, f.getchildren()[3].text,'en-US')):
                os.makedirs(os.path.join(SDCopy, f.getchildren()[3].text,'en-US'))
            if os.path.exists(sdfile):
                if not os.path.exists(targetfile):
                    shutil.copy2(sdfile,targetfile)

def sd2gitNoEnUS(Master,Component,EOLfile):

    root = ET.parse(EOLfile).getroot()


    #".//ItemGroup/..[@name='PowerApps-CDM-Entities']"
    #xpathExpression=('.//ItemGroup/..[@name="%s"]' %Component)
    print('.//ItemGroup/..[@name="%s"]' %Component)
    coms=root.findall('.//ItemGroup/..[@name="%s"]' %Component)
    for c in coms:
        files=c.findall("./ItemGroup/File")
        for f in files:
            print(f.get('name'))

            sdfile=os.path.join(Master,Component,f.get('name'))
            print('From ' +sdfile)
            targetfile=os.path.join(SDCopy, f.getchildren()[3].text,f.get('name'))
            print('To ' +targetfile)
            print('')
            if not os.path.exists(os.path.join(SDCopy, f.getchildren()[3].text)):
                os.makedirs(os.path.join(SDCopy, f.getchildren()[3].text))
            if os.path.exists(sdfile):
                if not os.path.exists(targetfile):
                    shutil.copy2(sdfile,targetfile)    

def sd2gitNoEnUS4TalentEngagement(Master,Component,EOLfile):

    root = ET.parse(EOLfile).getroot()


    #".//ItemGroup/..[@name='PowerApps-CDM-Entities']"
    #xpathExpression=('.//ItemGroup/..[@name="%s"]' %Component)
    print('.//ItemGroup/..[@name="%s"]' %Component)
    coms=root.findall('.//ItemGroup/..[@name="%s"]' %Component)
    for c in coms:
        files=c.findall("./ItemGroup/File")
        for f in files:
            print(f.get('name'))
            #adding talentEngagement folder
            sdfile=os.path.join(Master,'TalentEngagement',Component,f.get('name'))
            print('From ' +sdfile)
            targetfile=os.path.join(SDCopy, f.getchildren()[3].text,f.get('name'))
            print('To ' +targetfile)
            print('')
            if not os.path.exists(os.path.join(SDCopy, f.getchildren()[3].text)):
                os.makedirs(os.path.join(SDCopy, f.getchildren()[3].text))
            if os.path.exists(sdfile):
                if not os.path.exists(targetfile):
                    shutil.copy2(sdfile,targetfile) 


def sd2gitNoEnUS4OfficeApp(Master,Component,EOLfile):

    root = ET.parse(EOLfile).getroot()


    #".//ItemGroup/..[@name='PowerApps-CDM-Entities']"
    #xpathExpression=('.//ItemGroup/..[@name="%s"]' %Component)
    print('.//ItemGroup/..[@name="%s"]' %Component)
    coms=root.findall('.//ItemGroup/..[@name="%s"]' %Component)
    for c in coms:
        files=c.findall("./ItemGroup/File")
        for f in files:
            print(f.get('name'))
            #adding talentEngagement folder
            sdfile=os.path.join(Master,f.get('name'))
            print('From ' +sdfile)
            targetfile=os.path.join(SDCopy, f.getchildren()[3].text,f.get('name'))
            print('To ' +targetfile)
            print('')
            if not os.path.exists(os.path.join(SDCopy, f.getchildren()[3].text)):
                os.makedirs(os.path.join(SDCopy, f.getchildren()[3].text))
            if os.path.exists(sdfile):
                if not os.path.exists(targetfile):
                    shutil.copy2(sdfile,targetfile)
                    
########Taleng Engagement files#
sd2gitNoEnUS4TalentEngagement(r'C:\Depots\MBSI\Projects\OOB\UI\Master\source','Dynamics365-HCM-MsAssessClient',r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol')
sd2gitNoEnUS4TalentEngagement(r'C:\Depots\MBSI\Projects\OOB\UI\Master\source','Dynamics365-HCM-TalentEngagement',r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol')
sd2gitNoEnUS4TalentEngagement(r'C:\Depots\MBSI\Projects\OOB\UI\Master\source','Dynamics365-HCM-OnboardingClient',r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol')
sd2gitNoEnUS4TalentEngagement(r'C:\Depots\MBSI\Projects\OOB\UI\Master\source','Dynamics365-HCM-AppsPortalClient',r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol')
sd2gitNoEnUS4TalentEngagement(r'C:\Depots\MBSI\Projects\OOB\UI\Master\source','Dynamics365-HCM-OfferManagement',r'C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol')
#########HCM files##############
sd2git(r'C:\Depots\MBSI\Projects\OOB\UI\Master\source','HCMApp',r'C:\Depots\MBSI\Projects\OOB\UI\OOBApps.eol')

#########CDM files##############
sd2git(r'C:\Depots\MBSI\Projects\CDM\UI\Master\source','PowerApps-CDM-Entities',r'C:\Depots\MBSI\Projects\CDM\UI\CDM_UITest.eol')
##
sd2gitNoEnUS(r'C:\Depots\MBSI\Projects\CDM\UI\Master\source','cdm-outlook-addin',r'C:\Depots\MBSI\Projects\CDM\UI\CDM_UITest.eol')
##
sd2gitNoEnUS(r'C:\Depots\MBSI\Projects\CDM\UI\Master\source','client-control-lib',r'C:\Depots\MBSI\Projects\CDM\UI\CDM_UITest.eol')
##
sd2gitNoEnUS(r'C:\Depots\MBSI\Projects\CDM\UI\Master\source','Metadata',r'C:\Depots\MBSI\Projects\CDM\UI\CDM_UITest.eol')
##
sd2gitNoEnUS(r'C:\Depots\MBSI\Projects\CDM\UI\Master\source','Connector',r'C:\Depots\MBSI\Projects\CDM\UI\CDM_UITest.eol')
##
sd2gitNoEnUS(r'C:\Depots\MBSI\Projects\CDM\UI\Master\source','Discovery',r'C:\Depots\MBSI\Projects\CDM\UI\CDM_UITest.eol')

########AX7.x_OfficeApps files##########
sd2gitNoEnUS4OfficeApp(r'C:\Depots\MBSI\Projects\AX\7.x_OfficeApps\UI\Master\OfficeApps\Source','AX7.x_OfficeApps',r'C:\Depots\MBSI\Projects\AX\7.x_OfficeApps\UI\AX7.x_OfficeApp_UI.eol')
