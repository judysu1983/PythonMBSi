import os, shutil,stat

#Copy files from sd to git folder structure by C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol:
#e.g. from C:\Depots\MBSI\Projects\OOB\UI\ar\HcmApp\HCM.en-US.label.txt.lcl
#     to C:\GitProjects\HCM\source\Translation\LCL\ar\HCM.en-US.label.txt.lcl
#f= Accounting Foundation\source\metadata\Calendar\Calendar\AxLabelFile\LabelResources
langs=["ar","cs","da","de","de-AT","de-CH","en-AU","en-CA","en-GB","en-IE","en-IN","en-MY","en-NZ","en-SG","en-ZA","es","es-MX","et","fi","fr","fr-BE","fr-CA","fr-CH","hu","is","it","it-CH","ja","lt","lv","nb-NO","nl","nl-BE","pl","pt-BR","ru","sv","th","tr","zh-Hans"]
HCMfiles=["PersonnelUpgrade.en-US.label.txt.lcl","UserDefinedApp.en-US.label.txt.lcl","Benefits.en-US.label.txt.lcl","BusinessProcess.en-US.label.txt.lcl","CaseManagement.en-US.label.txt.lcl","Compensation.en-US.label.txt.lcl","HCM.en-us.label.txt.lcl","HcmACA.en-US.label.txt.lcl","HcmGenericProcess.en-US.label.txt.lcl","HcmMobile.en-US.label.txt.lcl","HcmOnboard.en-US.label.txt.lcl","HcmPeopleNavigatorControl.en-US.label.txt.lcl","HcmPeopleSearchControl.en-US.label.txt.lcl","HcmPersonCard.en-US.label.txt.lcl","HumanCapitalManagement.en-US.label.txt.lcl","Leave.en-US.label.txt.lcl","Payroll.en-US.label.txt.lcl","Personnel.en-US.label.txt.lcl","PersonnelBusinessProcess.en-US.label.txt.lcl","PersonnelCore.en-US.label.txt.lcl","Talent.en-US.label.txt.lcl","TalentClient.en-US.label.txt.lcl","TimeAtt.en-US.label.txt.lcl","Workforce.en-US.label.txt.lcl"]
ApplicationCommonfiles=["ApplicationCommon.en-US.label.txt.lcl","GetStarted.en-US.label.txt.lcl","GlobalAddressBook.en-US.label.txt.lcl","HierarchicalGridCommon.en-US.label.txt.lcl","SysBasicUpgrade.en-US.label.txt.lcl","SysPolicy.en-US.label.txt.lcl","UnitOfMeasure.en-US.label.txt.lcl","UserDefinedFields.en-US.label.txt.lcl","SysSecReportLabels.en-US.label.txt.lcl","ContactPersonManagement.en-US.label.txt.lcl"]
ApplicationIntegrationfiles=["CDSIntegration.en-US.label.txt.lcl"]
AccountingFoundationfiles=["BankAccountType.en-US.label.txt.lcl","Calendars.en-US.label.txt.lcl","CurrencyExchange.en-US.label.txt.lcl","Dimension.en-US.label.txt.lcl"]#"FieldDescriptions_GeneralLedger_Currency.en-US.label.txt.lcl"
ElectronicReportingfiles=["ElectronicReporting.en-US.label.txt.lcl","ElectronicReportingCore.en-US.label.txt.lcl","ElectronicReportingForAx.en-US.label.txt.lcl","ElectronicReportingMapping.en-US.label.txt.lcl","ElectronicReportingPrintManagementIntegration.en-US.label.txt.lcl","TaxEngine.en-US.label.txt.lcl","TaxEngineConfiguration.en-US.label.txt.lcl","TaxEngineInterface.en-US.label.txt.lcl","ElectronicReportingRetail.en-US.label.txt.lcl","ElectronicReportingRetailForAx.en-US.label.txt.lcl","TaxSettlement.en-US.label.txt.lcl"]


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    
def copyLCL(Component,fileList):

    GitLCLpath=os.path.join('C:\\test\HCMHB\\')+Component+'\\source\\Translation\\LCL'
    print(GitLCLpath)


    #remove all the files under C:\SourceMonitor\SDCopy    
    if os.path.exists(GitLCLpath):
        shutil.rmtree(GitLCLpath, onerror=del_rw)
    os.makedirs(GitLCLpath)

    SDpath=r'C:\Depots\MBSI\Projects\OOB\UI'
    for lang in langs:
        for f in fileList:
            print('copy LCL for: '+lang+': '+f)
            sdpath=os.path.join(SDpath,lang,'HcmApp')
            dstpath=os.path.join(GitLCLpath,lang)
            if not os.path.exists(dstpath):
                os.makedirs(dstpath)
            if os.path.exists(sdpath):
                print(os.path.join(dstpath,f))
                shutil.copy2(os.path.join(sdpath,f),os.path.join(dstpath,f))



copyLCL('HCM',HCMfiles)
copyLCL('ApplicationCommon',ApplicationCommonfiles)

copyLCL('ApplicationIntegration',ApplicationIntegrationfiles)
copyLCL('ElectronicReporting',ElectronicReportingfiles)
copyLCL('Accounting Foundation',AccountingFoundationfiles)
