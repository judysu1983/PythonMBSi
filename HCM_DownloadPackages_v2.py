# -*- coding: cp1252 -*-
import os, shutil, sys, stat


##Microsoft.Dynamics.AX.ApplicationCommonProd.Translations.7.2.3021
##Microsoft.Dynamics.AX.AccountingFoundationPartialProd.Translations.7.2.3019
##Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations.7.2.3010
##Microsoft.Dynamics.AX.ElectronicReportingPartialProd.Translations.7.2.3012
##Microsoft.Dynamics.AX.HCMProd.Translations.7.2.3040

##nuget install Microsoft.Dynamics.AX.ApplicationCommonProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version 7.2.10
##nuget install Microsoft.Dynamics.AX.AccountingFoundationPartialProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v2" -Version 7.2.7
##nuget install Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version 7.2.3011 
##nuget install Microsoft.Dynamics.AX.ElectronicReportingPartialProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version 7.2.7
##nuget install Microsoft.Dynamics.AX.HCMProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version 7.2.10
def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

   
packagepath=r'C:\SourceMonitor\P'

if os.path.exists(packagepath):
    shutil.rmtree(packagepath, onerror=del_rw)
os.makedirs(packagepath)
os.chdir(packagepath)



NuGetpackagepath=r'C:\Python27\NuGetPackages'
subdirs=os.listdir(NuGetpackagepath)
print(subdirs)
#['Microsoft.Dynamics.AX.AccountingFoundationProd.Translations.8.1.57', 'Microsoft.Dynamics.AX.ApplicationCommonProd.Translations.8.1.28', 'Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations.8.1.28', 'Microsoft.Dynamics.AX.ElectronicReportingProd.Translations.8.1.21', 'Microsoft.Dynamics.AX.HCMProd.Translations.8.1.123']
#C:\test\NuGetPackages\Microsoft.Dynamics.AX.HCMProd.Translations.8.1.123\Metadata
# to C:\Gitprojects\HCM\source\metadata

AccountingFoundationpath1=os.path.join(NuGetpackagepath+'\\'+subdirs[0]+'\Metadata')
shutil.copytree(AccountingFoundationpath1, 'C:\SourceMonitor\P\Accounting Foundation\source\Metadata')

ApplicationCommonpath1=os.path.join(NuGetpackagepath+'\\'+subdirs[1]+'\Metadata')
shutil.copytree(ApplicationCommonpath1, 'C:\SourceMonitor\P\ApplicationCommon\source\Metadata')

ApplicationIntegrationpath1=os.path.join(NuGetpackagepath+'\\'+subdirs[2]+'\Metadata')
shutil.copytree(ApplicationIntegrationpath1, 'C:\SourceMonitor\P\ApplicationIntegration\source\Metadata')

ElectronicReportingpath1=os.path.join(NuGetpackagepath+'\\'+subdirs[3]+'\Metadata')
shutil.copytree(ElectronicReportingpath1, 'C:\SourceMonitor\P\ElectronicReporting\source\Metadata')


HCMpath1=os.path.join(NuGetpackagepath+'\\'+subdirs[4]+'\Metadata')
shutil.copytree(HCMpath1, 'C:\SourceMonitor\P\HCM\source\Metadata')

##
##version = ['8.1.104', '8.1.22', '8.1.23', '8.1.43', '8.1.14']
##
##hcmversion=version[0]
##print(hcmversion)
##os.system('nuget install Microsoft.Dynamics.AX.HCMProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json"  -NonInteractive -DirectDownload')
##os.rename('Microsoft.Dynamics.AX.HCMProd.Translations'+'.'+ hcmversion, 'source')
##os.makedirs('HCM')
##shutil.move('source','HCM')
##
##ApplicationCommonVersion=version[1]
##print(ApplicationCommonVersion)
##os.system('nuget install Microsoft.Dynamics.AX.ApplicationCommonProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version ' + ApplicationCommonVersion)
##os.rename('Microsoft.Dynamics.AX.ApplicationCommonProd.Translations'+'.'+ ApplicationCommonVersion, 'source')
##os.makedirs('ApplicationCommon')
##shutil.move('source','ApplicationCommon')
##
##ApplicationIntegrationversion=version[2]
##print(ApplicationIntegrationversion)
##os.system('nuget install Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version ' + ApplicationIntegrationversion)
##os.rename('Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations'+'.'+ ApplicationIntegrationversion, 'source')
##os.makedirs('ApplicationIntegration')
##shutil.move('source','ApplicationIntegration')
##
##
##AccountingFoundationversion=version[3]
##print(AccountingFoundationversion)
##os.system('nuget install Microsoft.Dynamics.AX.AccountingFoundationProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -version ' + AccountingFoundationversion)
##os.rename('Microsoft.Dynamics.AX.AccountingFoundationProd.Translations'+'.'+ AccountingFoundationversion, 'source')
##os.makedirs('Accounting Foundation')
##shutil.move('source','Accounting Foundation')
##
##
##ElectronicReportingVersion=version[4]
##print(ElectronicReportingVersion)
##os.system('nuget install Microsoft.Dynamics.AX.ElectronicReportingProd.Translations -source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -version ' + ElectronicReportingVersion)
##os.rename('Microsoft.Dynamics.AX.ElectronicReportingProd.Translations'+'.'+ ElectronicReportingVersion, 'source')
##os.makedirs('ElectronicReporting')
##shutil.move('source','ElectronicReporting')

















