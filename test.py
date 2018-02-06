import shutil, os
#files=['Payroll', 'Personnel', 'Benefits', 'Compensation', 'FieldDescriptions_Hcm', 'HcmACA', 'Talent', 'Workforce', 'HcmMobile', 'PersonnelTasks', 'TimeAtt', 'BusinessProcess', 'HumanCapitalManagement', 'CaseManagement', 'TalentClient', 'HCM', 'Dimension', 'Calendars', 'CurrencyExchange', 'FieldDescriptions_GeneralLedger_Currency', 'HierarchicalGridCommon', 'SysPolicy', 'UnitOfMeasure', 'GlobalAddressBook', 'ElectronicReportingPrintManagementIntegration', 'ElectronicReportingCore', 'ElectronicReportingMapping', 'ElectronicReporting', 'UserDefinedFields']
langs=["zh-Hans","ar","cs","da","de","de-AT","de-CH","en-AU","en-CA","en-GB","en-IE","en-IN","en-MY","en-NZ","en-SG","en-ZA","es","es-MX","et","fi","fr","fr-BE","fr-CA","fr-CH","hu","is","it","it-CH","ja","lt","lv","Master","nb-NO","nl","nl-BE","pl","pt-BR","ru","sv","th","tr"]


#Copy from 
#C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI\ar\AppResources.en-US.resx.lcl
#C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI\ar\DemoDataResources.en-US.resx.lcl
#copy to:
#C:\Depots\MBSI\Projects\OOB\UI\ar\WarehouseMobileApp\AppResources.en-US.resx.lcl
#C:\Depots\MBSI\Projects\OOB\UI\ar\WarehouseMobileApp\DemoDataResources.en-US.resx.lcl
OOBRoot='C:\Depots\MBSI\Projects\OOB\UI'

for lang in langs:
    print(lang)
    
    #target folder of the *.en-US.label.txt.lcl file
    PathTarget=os.path.join(OOBRoot,lang,'WarehouseMobileApp')
    if not os.path.exist(PathTarget):
    	os.makedirs(PathTarget)
    shutil.copy2(os.path.join('C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI',lang,'AppResources.en-US.resx.lcl'),os.path.join(PathTarget,'AppResources.en-US.resx.lcl'))
    	
    for f1 in UAfiles:
        dllf1=f1+".resources.dll.lcl"
        labelf1=f1+".en-US.label.txt.lcl"
        print(os.path.join(AX7UApath,lang,'Application',dllf1))
        if os.path.isfile(os.path.join(AX7UApath,lang,'Application',dllf1)):
            print(dllf1)
            if not os.path.exists(HCMAppPathTarget):
                os.makedirs(HCMAppPathTarget)
            shutil.copy2(os.path.join(AX7UApath,lang,'Application', dllf1),os.path.join(HCMAppPathTarget,labelf1))
