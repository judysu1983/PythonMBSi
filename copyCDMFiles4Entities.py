import shutil, os
files=["CustomerService","Foundation","Group","Organization","Person","Purchase","Sales","SurveySecurity"]
langs=["sr-Latn-RS", "sv", "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant", "bg", "ca-ES", "cs", "da", "de", "el", "es", "et", "eu", "fi", "fr", "gl", "hi", "hr-HR", "hu", "id", "it", "ja", "kk", "ko", "lt", "lv", "ms-MY", "nb-NO", "nl", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sl", "sr-Cyrl-RS"]
#langs=['master']
AX7path='C:\\test\\CDM'
HCMAppPath='C:\\test\\CDMUI'


####copy UI files#####
# copy from AX7path\bg\PowerApps-CDM-Entities\CustomerService.resources.dll.lcl
# copy to    HCMAppPath\bg\PowerApps-CDM-Entities\CustomerService.label.txt.lcl
for lang in langs:
   #target folder of the *.en-US.label.txt.lcl file
   for f1 in files:
       dllf1=f1+".resources.dll.lcl"
       labelf1=f1+".en-US.label.txt.lcl"
       print(os.path.join(AX7path,lang,'PowerApps-CDM-Entities',dllf1))
       if os.path.isfile(os.path.join(AX7path,lang,'PowerApps-CDM-Entities',dllf1)):
           print(dllf1)

           shutil.copy2(os.path.join(AX7path,lang,'PowerApps-CDM-Entities',dllf1),os.path.join(HCMAppPath,lang,'PowerApps-CDM-Entities',labelf1))

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

# #####copy UA master#####
# UAfiles=['FieldDescriptions_GeneralLedger_Currency']
# AX7UApath='C:\\Depots\\MBSI\\Projects\\AX\\7.x\\UA\\Field_Descriptions'
# HCMAppUAPath='C:\\Depots\\MBSI\\Projects\\OOB\\UA\\Field_Descriptions'
# ####copy UA files####
# #copy from C:\Depots\MBSI\Projects\AX\7.x\UA\Field_Descriptions\ja\Application\*.resources.dll.lcl
# #copy to    C:\Depots\MBSI\Projects\OOB\UA\Field_Descriptions\ja\HcmApp\*.en-US.label.txt.lcl
# for lang in langs:
#    print(lang)
#    #target folder of the *.en-US.label.txt.lcl file
#    HCMAppPathTarget=os.path.join(HCMAppUAPath,'Master','HcmApp','SrcLCX')
#    for f1 in UAfiles:
#        dllf1=f1+".resources.dll.lcg"
#        labelf1=f1+".en-US.label.txt.lcg"
#        print(os.path.join(AX7UApath,lang,'Application','SrcLCX',dllf1))
#        if os.path.isfile(os.path.join(AX7UApath,lang,'Application','SrcLCX',dllf1)):
#            print(dllf1)
#            if not os.path.exists(HCMAppPathTarget):
#                os.makedirs(HCMAppPathTarget)
#            shutil.copy2(os.path.join(AX7UApath,lang,'Application','SrcLCX',dllf1),os.path.join(HCMAppPathTarget,labelf1))


# #####copy UA master#####
# UAfiles=['FieldDescriptions_GeneralLedger_Currency']
# AX7UApath='C:\\Depots\\MBSI\\Projects\\AX\\7.x\\UA\\Field_Descriptions'
# HCMAppUAPath='C:\\Depots\\MBSI\\Projects\\OOB\\UA\\Field_Descriptions'
# ####copy UA files####
# #copy from C:\Depots\MBSI\Projects\AX\7.x\UA\Field_Descriptions\ja\Application\*.resources.dll.lcl
# #copy to    C:\Depots\MBSI\Projects\OOB\UA\Field_Descriptions\ja\HcmApp\*.en-US.label.txt.lcl
# for lang in langs:
#     print(lang)
#     #target folder of the *.en-US.label.txt.lcl file
#     HCMAppPathTarget=os.path.join(HCMAppUAPath,lang,'HcmApp')
#     for f1 in UAfiles:
#         dllf1=f1+".resources.dll.lcl"
#         labelf1=f1+".en-US.label.txt.lcl"
#         print(os.path.join(AX7UApath,lang,'Application',dllf1))
#         if os.path.isfile(os.path.join(AX7UApath,lang,'Application',dllf1)):
#             print(dllf1)
#             if not os.path.exists(HCMAppPathTarget):
#                 os.makedirs(HCMAppPathTarget)
#             shutil.copy2(os.path.join(AX7UApath,lang,'Application', dllf1),os.path.join(HCMAppPathTarget,labelf1))
