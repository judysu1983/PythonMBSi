import os, shutil,stat

#Copy files from sd to git folder structure by C:\Depots\MBSI\Projects\OOB\UI\OOBAppsTest.eol:
#e.g. from C:\Depots\MBSI\Projects\OOB\UI\ar\HcmApp\HCM.en-US.label.txt.lcl
#     to C:\GitProjects\HCM\source\Translation\LCL\ar\HCM.en-US.label.txt.lcl
#f= Accounting Foundation\source\metadata\Calendar\Calendar\AxLabelFile\LabelResources
langs=["ar","ar-AE","cs","da","de","de-AT","de-CH","en-AU","en-CA","en-GB","en-IE","en-IN","en-MY","en-NZ","en-SG","en-ZA","es","es-MX","et","fi","fr","fr-BE","fr-CA","fr-CH","hu","is","it","it-CH","ja","lt","lv","nb-NO","nl","nl-BE","pl","pt-BR","ru","sv","th","tr","zh-Hans"]
HCMfiles=["UserDefinedApp.en-US.label.txt.lcl", "BusinessProcess.en-US.label.txt.lcl", "CaseManagement.en-US.label.txt.lcl", "HcmPeopleNavigatorControl.en-US.label.txt.lcl", "HcmPeopleSearchControl.en-US.label.txt.lcl", "HcmPersonCard.en-US.label.txt.lcl", "HumanCapitalManagement.en-US.label.txt.lcl", "HumanCapitalMobile.en-US.label.txt.lcl", "Leave.en-US.label.txt.lcl", "Personnel.en-US.label.txt.lcl", "HcmOnboard.en-US.label.txt.lcl", "PersonnelBusinessProcess.en-US.label.txt.lcl", "PersonnelCore.en-US.label.txt.lcl", "Benefits.en-US.label.txt.lcl", "Compensation.en-US.label.txt.lcl", "HCM.en-us.label.txt.lcl", "HcmACA.en-US.label.txt.lcl", "HcmGenericProcess.en-US.label.txt.lcl", "Payroll.en-US.label.txt.lcl", "Talent.en-US.label.txt.lcl", "TalentClient.en-US.label.txt.lcl", "Workforce.en-US.label.txt.lcl", "HcmMobile.en-US.label.txt.lcl", "PersonnelUpgrade.en-US.label.txt.lcl", "TimeAtt.en-US.label.txt.lcl"]
ApplicationCommonfiles=["ApplicationCommon.en-US.label.txt.lcl", "GetStarted.en-US.label.txt.lcl", "HierarchicalGridCommon.en-US.label.txt.lcl", "ContactPersonManagement.en-US.label.txt.lcl", "Directory_InvoicesCommunication.en-US.label.txt.lcl", "GlobalAddressBook_App73Hotfix.en-US.label.txt.lcl", "GlobalAddressBook.en-US.label.txt.lcl", "SysSecReportLabels.en-US.label.txt.lcl", "DirectoryUpgrade.en-US.label.txt.lcl", "SysPolicy.en-US.label.txt.lcl", "SysBasicUpgrade.en-US.label.txt.lcl", "UnitOfMeasure.en-US.label.txt.lcl", "UserDefinedFields.en-US.label.txt.lcl"]

CostAccountingfiles=["CostAccounting.en-US.label.txt.lcl"]
AccountingFoundationfiles=["BankAccountType.en-US.label.txt.lcl", "Calendars.en-US.label.txt.lcl", "CurrencyCodesDynamics_3945654.en-US.label.txt.lcl", "CurrencyExchange.en-US.label.txt.lcl", "Dimension.en-US.label.txt.lcl", "DimensionSegmentSeparator.en-US.label.txt.lcl", "Ledger.en-US.label.txt.lcl", "LedgerEntity.en-US.label.txt.lcl", "SegmentedEntry.en-US.label.txt.lcl", "Measurement.en-US.label.txt.lcl", "AccountingFramework.en-US.label.txt.lcl", "SourceDocumentation.en-US.label.txt.lcl", "TaxEngineIntegration_SourceDocumentation.en-US.label.txt.lcl", "TaxEngineIntegration_SourceDocumentationTypes.en-US.label.txt.lcl", "Subledger.en-US.label.txt.lcl"]
#AccountingFoundationfiles=["Ledger.en-us.label.txt.lcl", "Measurement.en-us.label.txt.lcl", "AccountingFramework.en-us.label.txt.lcl", "SourceDocumentation.en-us.label.txt.lcl", "TaxEngineIntegration_SourceDoc.en-us.label.txt.lcl", "TaxEngineIntegration_SourceDocTypes.en-us.label.txt.lcl", "Subledger.en-us.label.txt.lcl"]
#ElectronicReportingfiles=["ElectronicReporting.en-US.label.txt.lcl", "ElectronicReportingPrintManagementIntegration.en-US.label.txt.lcl", "ElectronicReportingCore.en-US.label.txt.lcl", "ElectronicReportingForAx.en-US.label.txt.lcl", "ElectronicReportingMapping.en-US.label.txt.lcl", "ElectronicReportingRetail.en-US.label.txt.lcl", "ElectronicReportingRetailForAx.en-US.label.txt.lcl", "TaxEngine.en-US.label.txt.lcl", "TaxEngineConfiguration.en-US.label.txt.lcl", "TaxEngineInterface.en-US.label.txt.lcl", "TaxSettlement.en-US.label.txt.lcl"]

ElectronicReportingfiles=["ElectronicReporting.en-US.label.txt.lcl","ElectronicReportingMapping.en-US.label.txt.lcl"]


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    
def copyLCL(Component,fileList):

    GitLCLpath=os.path.join('C:\\test\App73HB\\')+Component+'\\source\\Translation\\LCL'
    print(GitLCLpath)


    #remove all the files under C:\SourceMonitor\SDCopy    
    if os.path.exists(GitLCLpath):
        shutil.rmtree(GitLCLpath, onerror=del_rw)
    os.makedirs(GitLCLpath)

    SDpath=r'C:\Depots\MBSI\Projects\OOB\App7x\UI'
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


##
##copyLCL('HCM',HCMfiles)
##copyLCL('ApplicationCommon',ApplicationCommonfiles)
copyLCL('ElectronicReporting',ElectronicReportingfiles)
##copyLCL('Cost%20Accounting',CostAccountingfiles)
##copyLCL('Accounting%20Foundation',AccountingFoundationfiles)
