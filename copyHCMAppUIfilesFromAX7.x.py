import shutil, os
files=['DirectoryUpgrade']
langs=['ar', 'cs', 'da', 'de', 'de-AT', 'de-CH', 'en-AU', 'en-CA', 'en-GB', 'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-SG', 'en-US', 'en-ZA', 'es', 'es-MX', 'et', 'fi', 'fr', 'fr-BE', 'fr-CA', 'fr-CH', 'hu', 'is', 'it', 'it-CH', 'ja', 'lt', 'lv', 'Master', 'nb-NO', 'nl', 'nl-BE', 'pl', 'pt-BR', 'ru', 'sv', 'th', 'tr', 'zh-Hans']
#langs=['master']
AX7path='C:\\Depots\\MBSI\\Projects\\AX\\7.x\\UI'
HCMAppPath='C:\\Test\\AccountingFoundation0111'


###copy UI files#####
##copy from C:\Depots\MBSI\Projects\AX\7.x\UI\ja\Application\Payroll.resources.dll.lcl
##copy to    C:\Depots\MBSI\Projects\OOB\Test(UI)\ja\HcmApp\Payroll.en-US.label.txt.lcl
for lang in langs:
    #target folder of the *.en-US.label.txt.lcl file
    HCMAppPathTarget=os.path.join(HCMAppPath,lang,'HcmApp')
    for f1 in files:
        dllf1=f1+".resources.dll.lcl"
        labelf1=f1+".en-US.label.txt.lcl"
        if os.path.isfile(os.path.join(AX7path,lang,'Application',dllf1)):
            print(dllf1)
            if not os.path.exists(HCMAppPathTarget):
                os.makedirs(HCMAppPathTarget)
            shutil.copy2(os.path.join(AX7path,lang,'Application',dllf1),os.path.join(HCMAppPath,lang,'HcmApp',labelf1))

######copy master files####
###copy from C:\Depots\MBSI\Projects\AX\7.x\UI\ja\Application\SrcLCX\Payroll.resources.dll.lcl
###copy to    C:\Depots\MBSI\Projects\OOB\Test(UI)\ja\HcmApp\Payroll.en-US.label.txt.lcl
##for lang in langs:
##    print(lang)
##    #target folder of the *.en-US.label.txt.lcl file
##    HCMAppPathTarget=os.path.join(HCMAppPath,'Master','HcmApp','SrcLCX')
##    for f1 in files:
##        dllf1=f1+".resources.dll.lcg"
##        labelf1=f1+".en-US.label.txt.lcg"
##        if os.path.isfile(os.path.join(AX7path,lang,'Application','SrcLCX',dllf1)):
##            print(dllf1)
##            if not os.path.exists(HCMAppPathTarget):
##                os.makedirs(HCMAppPathTarget)
##            shutil.copy2(os.path.join(AX7path,lang,'Application','SrcLCX',dllf1),os.path.join(HCMAppPathTarget,labelf1))

#####copy UA master#####
##UAfiles=['FieldDescription_Ledger']
##AX7UApath='C:\\Depots\\MBSI\\Projects\\AX\\7.x\\UA\\Field_Descriptions'
##HCMAppUAPath='C:\\test\\UA\\Field_Descriptions'
####copy UA files####
##copy from C:\Depots\MBSI\Projects\AX\7.x\UA\Field_Descriptions\ja\Application\*.resources.dll.lcl
##copy to    C:\Depots\MBSI\Projects\OOB\UA\Field_Descriptions\ja\HcmApp\*.en-US.label.txt.lcl
##for lang in langs:
##    print(lang)
##    #target folder of the *.en-US.label.txt.lcl file
##    HCMAppPathTarget=os.path.join(HCMAppUAPath,'Master','HcmApp','SrcLCX')
##    for f1 in UAfiles:
##        dllf1=f1+".resources.dll.lcl"
##        labelf1=f1+".en-US.label.txt.lcl"
##        print(os.path.join(AX7UApath,lang,'Application','SrcLCX',dllf1))
##        if os.path.isfile(os.path.join(AX7UApath,lang,'Application','SrcLCX',dllf1)):
##            print(dllf1)
##            if not os.path.exists(HCMAppPathTarget):
##                os.makedirs(HCMAppPathTarget)
##            shutil.copy2(os.path.join(AX7UApath,lang,'Application','SrcLCX',dllf1),os.path.join(HCMAppPathTarget,labelf1))


#####copy UA master#####
##UAfiles=['FieldDescriptions_Ledger']
##AX7UApath='C:\\Depots\\MBSI\\Projects\\AX\\7.x\\UA\\Field_Descriptions'
##HCMAppUAPath='C:\\test\\OOB\\UA\\Field_Descriptions'
####copy UA files####
##copy from C:\Depots\MBSI\Projects\AX\7.x\UA\Field_Descriptions\ja\Application\*.resources.dll.lcl
##copy to    C:\Depots\MBSI\Projects\OOB\UA\Field_Descriptions\ja\HcmApp\*.en-US.label.txt.lcl
##for lang in langs:
##    #print(lang)
##    #target folder of the *.en-US.label.txt.lcl file
##    HCMAppPathTarget=os.path.join(HCMAppUAPath,lang,'HcmApp')
##    for f1 in UAfiles:
##        dllf1=f1+".resources.dll.lcl"
##        labelf1=f1+".en-US.label.txt.lcl"
##        print(os.path.join(AX7UApath,lang,'Application',dllf1))
##        if os.path.isfile(os.path.join(AX7UApath,lang,'Application',dllf1)):
##            print(dllf1)
##            if not os.path.exists(HCMAppPathTarget):
##                os.makedirs(HCMAppPathTarget)
##                print(HCMAppPathTarget)
##            shutil.copy2(os.path.join(AX7UApath,lang,'Application', dllf1),os.path.join(HCMAppPathTarget,labelf1))
