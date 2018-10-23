import os, shutil, stat, sys
langs=["ar", "cs", "da", "de-at", "de-ch", "de", "en-au", "en-ca", "en-gb", "en-ie", "en-in", "en-my", "en-nz", "en-sg", "en-us", "en-za", "es", "es-mx", "et", "fi", "fr-be", "fr-ca", "fr-ch", "fr", "he", "hu", "is", "it-CH", "it", "ja", "lt", "lv", "nb-NO", "nl-BE", "nl", "pl", "pt-br", "ru", "sv", "th", "tr", "zh-hans"]

langs2=["ar-SA", "cs-CZ", "da-dk", "de-at", "de-ch", "de-de", "en-au", "en-ca", "en-gb", "en-ie", "en-in", "en-my", "en-nz", "en-sg", "en-us", "en-za", "es-es", "es-mx", "et-EE", "fi-FI", "fr-be", "fr-ca", "fr-ch", "fr-fr", "he-IL", "hu-HU", "is-IS", "it-CH", "it-it", "ja-jp", "lt-LT", "lv-LV", "nb-NO", "nl-BE", "nl-nl", "pl-PL", "pt-br", "ru-ru", "sv-SE", "th-TH", "tr-TR", "zh-hans"]
#  files=["MRUpdate.resources.dll.lcl","Microsoft.Dynamics.Performance.Reporting.Engine.Client.resources.dll.lcl","Microsoft.Dynamics.Performance.DataProvider.EntityWizard.resources.dll.lcl","Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.Navigation.AX6.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.Office.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.ApplicationService.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.AX.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.Database.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.DataMart.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.Integration.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.Service.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.CompanyConfiguration.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.CompanyImport.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Connector.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Console.Core.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Database.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.AX.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.DataMart.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.GP.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.NAV.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Reporting.resources.dll.lcl", "Microsoft.Dynamics.Performance.Integration.Message.resources.dll.lcl", "Microsoft.Dynamics.Performance.Platform.Client.Cloud.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataAccess.Server.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataAccess.Service.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataProvider.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Engine.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Migration.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.NativeReport.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.NativeReport.Server.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Repository.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Repository.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Resources.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Security.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Security.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Viewer.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Viewer.Pipelines.Native.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Xbrl.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.WizardFramework.resources.dll.lcl", "Microsoft.Dynamics.Performance.Xbrl.resources.dll.lcl", "MigrationWizard.resources.dll.lcl", "MigrationWizardStrings.wxl.lcl", "MR_MSLT.rtf", "MRConfigurationConsole.resources.dll.lcl", "MRLaunch.resources.dll.lcl", "ReportDesigner.resources.dll.lcl", "ReportViewer.resources.dll.lcl", "ServerStrings.wxl.lcl", "Strings.wxl.lcl", "WixExtensionStrings.wxl.lcl", "ClientStrings.wxl.lcl", "CommonStrings.wxl.lcl", "FinancialReportingDeployer.resources.dll.lcl", "ManagementReporter.chm", "Microsoft.Dynamics.Performance.Calculation.resources.dll.lcl", "Microsoft.Dynamics.Performance.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.Core.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.AX.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.AX6.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.DDM.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.GP.resources.dll.lcl"]
files=["Microsoft.Dynamics.Performance.Reporting.NativeReport.Server.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Repository.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Repository.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Resources.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Security.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Security.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Viewer.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Viewer.Pipelines.Native.resources.dll.lcl", "Microsoft.Dynamics.Performance.WizardFramework.resources.dll.lcl", "MigrationWizard.resources.dll.lcl", "MigrationWizardStrings.wxl.lcl", "MRConfigurationConsole.resources.dll.lcl", "MRLaunch.resources.dll.lcl", "ReportDesigner.resources.dll.lcl", "ReportViewer.resources.dll.lcl", "ServerStrings.wxl.lcl", "Strings.wxl.lcl", "WixExtensionStrings.wxl.lcl", "ClientStrings.wxl.lcl", "CommonStrings.wxl.lcl", "FinancialReportingDeployer.resources.dll.lcl", "Microsoft.Dynamics.Performance.Calculation.resources.dll.lcl", "Microsoft.Dynamics.Performance.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.Core.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.AX.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.DDM.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.GeneralLedger.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.Navigation.AX6.resources.dll.lcl", "Microsoft.Dynamics.Performance.DataProvider.Office.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.ApplicationService.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.AX.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.Database.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.Integration.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Commands.Service.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.CompanyConfiguration.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.CompanyImport.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Connector.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Console.Core.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Database.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.AX.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.DataMart.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.DataProvider.GP.resources.dll.lcl", "Microsoft.Dynamics.Performance.Deployment.Reporting.resources.dll.lcl", "Microsoft.Dynamics.Performance.Integration.Message.resources.dll.lcl", "Microsoft.Dynamics.Performance.Platform.Client.Cloud.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataAccess.Server.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataAccess.Service.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.DataProvider.Client.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Engine.Common.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.Migration.resources.dll.lcl", "Microsoft.Dynamics.Performance.Reporting.NativeReport.Client.resources.dll.lcl"]
def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
#copy from C:\Depots\MBSI\Projects\MR\AX8\UI\ar-SA\Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl
#to C:\test\MR\UI\ar\MR-Localization\Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl

Oldpath=r'C:\Depots\MBSI\Projects\MR\AX8\UI'
Testroot=r'C:\test\MR\UI'
gitpath='UI'
##def removefiles():
##    targetFolder=os.path.join(Testroot,gitpath)
##    for l in langs2:
##        targetFile=os.path.join(targetFolder,l,'resources.'+l+'.resx')
##        if os.path.isfile(targetFile):
##            print('remove: '+targetFile)
##            os.remove(targetFile)

def copyMR():
    i=0
    for lang in langs2:
        if os.path.exists(os.path.join(Oldpath,lang)):                
#copy from C:\Depots\MBSI\Projects\MR\AX8\UI\ar-SA\Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl
#to C:\test\MR\UI\ar\MR-Localization\Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl
            for f in files:
                oldLCLfile=os.path.join(Oldpath,lang,f)
                print(oldLCLfile)
                dst=os.path.join(Testroot,langs[i],'MR_Localization')
                
                if not os.path.exists(dst):
                    os.makedirs(dst)
                if os.path.exists(oldLCLfile):
                    shutil.copy2(oldLCLfile,os.path.join(dst,f))
            i=i+1

#copy from C:\test\HCMHB\Sep.4\source\Translation\LCL\de\Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl
# to C:\test\HCMHB\MR-Localization\de-de\Microsoft.Dynamics.Performance.Reporting.DataAccess.Client.resources.dll.lcl
#
SDcopiedpath=r'C:\test\HCMHB\Sep.4\source\Translation\LCL'
MRgitpath=r'C:\test\HCMHB\MR-Localization'
if os.path.exists(MRgitpath):
    shutil.rmtree(MRgitpath,onerror=del_rw)

def copyMR2Git():
    i=0
    for lang in langs:
        for f in files:
            HBfile=os.path.join(SDcopiedpath,lang,f)
            print(HBfile)
            dst=os.path.join(MRgitpath,langs2[i])
            print(dst)
            if not os.path.exists(dst):
                os.makedirs(dst)
            if os.path.exists(HBfile):
                shutil.copy2(HBfile,os.path.join(dst,f))
        i=i+1
#removefiles()
copyMR2Git()
