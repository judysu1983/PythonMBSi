import os, shutil,stat

#Copy files from sd to git folder structure by C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol:
#e.g. from C:\Depots\MBSI\Projects\OOB\UI\ar\HcmApp\HCM.en-US.label.txt.lcl
#     to C:\GitProjects\HCM\source\Translation\LCL\ar\HCM.en-US.label.txt.lcl
#f= Accounting Foundation\source\metadata\Calendar\Calendar\AxLabelFile\LabelResources
langs=["ar","cs","da","de","de-AT","de-CH","en-AU","en-CA","en-GB","en-IE","en-IN","en-MY","en-NZ","en-SG","en-ZA","es","es-MX","et","fi","fr","fr-BE","fr-CA","fr-CH","hu","is","it","it-CH","ja","lt","lv","nb-NO","nl","nl-BE","pl","pt-BR","ru","sv","th","tr","zh-Hans"]
HCMfiles=["FieldDescriptions_Hcm.en-US.label.txt.lcl"]
AccountingFoundationfiles=["FieldDescriptions_GeneralLedger_Currency.en-US.label.txt.lcl"]


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    
def copyLCL(Component,fileList):

    GitLCLpath=os.path.join('C:\\test\HCMHBUA\\')+Component+'\\source\\Translation\\LCL'
    print(GitLCLpath)


    #remove all the files under C:\SourceMonitor\SDCopy    
    if os.path.exists(GitLCLpath):
        shutil.rmtree(GitLCLpath, onerror=del_rw)
    os.makedirs(GitLCLpath)

    SDpath=r'C:\Depots\MBSI\Projects\OOB\UA\Field_Descriptions'
    for lang in langs:
        for f in fileList:
            print('copy LCL for: '+lang+': '+f)
            sdpath=os.path.join(SDpath,lang,'HcmApp')
            dstpath=os.path.join(GitLCLpath,lang)
            print(sdpath)
            print(dstpath)
            if not os.path.exists(dstpath):
                os.makedirs(dstpath)
            if os.path.exists(sdpath):
                print(os.path.join(dstpath,f))
                shutil.copy2(os.path.join(sdpath,f),os.path.join(dstpath,f))



copyLCL('HCM',HCMfiles)
copyLCL('Accounting Foundation',AccountingFoundationfiles)
