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

version = ['8.1.148-rainmain0004', '8.1.39', '8.1.7', '8.1.74', '8.1.33']

hcmversion=version[0]
print(hcmversion)
os.system('nuget install Microsoft.Dynamics.AX.HCMProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version ' + hcmversion)
os.rename('Microsoft.Dynamics.AX.HCMProd.Translations'+'.'+ hcmversion, 'source')
os.makedirs('HCM')
shutil.move('source','HCM')

ApplicationCommonVersion=version[1]
print(ApplicationCommonVersion)
os.system('nuget install Microsoft.Dynamics.AX.ApplicationCommonProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version ' + ApplicationCommonVersion)
os.rename('Microsoft.Dynamics.AX.ApplicationCommonProd.Translations'+'.'+ ApplicationCommonVersion, 'source')
os.makedirs('ApplicationCommon')
shutil.move('source','ApplicationCommon')

##ApplicationIntegrationversion=version[2]
##print(ApplicationIntegrationversion)
##os.system('nuget install Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version ' + ApplicationIntegrationversion)
##os.rename('Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations'+'.'+ ApplicationIntegrationversion, 'source')
##os.makedirs('ApplicationIntegration')
##shutil.move('source','ApplicationIntegration')
CostAccountingVersion=version[2]
print(CostAccountingVersion)
os.system('nuget install Microsoft.Dynamics.AX.CostAccountingProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -Version ' + CostAccountingVersion)
os.rename('Microsoft.Dynamics.AX.CostAccountingProd.Translations'+'.'+ CostAccountingVersion, 'source')
os.makedirs('CostAccounting')
shutil.move('source','CostAccounting')


AccountingFoundationversion=version[3]
print(AccountingFoundationversion)
os.system('nuget install Microsoft.Dynamics.AX.AccountingFoundationProd.Translations -Source "https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json" -version ' + AccountingFoundationversion)
os.rename('Microsoft.Dynamics.AX.AccountingFoundationProd.Translations'+'.'+ AccountingFoundationversion, 'source')
os.makedirs('Accounting Foundation')
shutil.move('source','Accounting Foundation')


ElectronicReportingVersion=version[4]
print(ElectronicReportingVersion)
os.system('nuget install Microsoft.Dynamics.AX.ElectronicReportingProd.Translations -source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -version ' + ElectronicReportingVersion)
os.rename('Microsoft.Dynamics.AX.ElectronicReportingProd.Translations'+'.'+ ElectronicReportingVersion, 'source')
os.makedirs('ElectronicReporting')
shutil.move('source','ElectronicReporting')

















