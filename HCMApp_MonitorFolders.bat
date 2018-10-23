@echo off
rem sync sd
rem copy sd files to git folder structure to C:\SourceMonitor\SDCopy
rem sync git
rem copy git files to C:\SourceMonitor\Gitcopy

rem set SDRoot=C:\Depots\MBSI\Projects\OOB\UI\Master
set SDRoot=C:\Depots\MBSI\Projects
set GitRoot=C:\GitProjects
set MonitorRoot1=C:\SourceMonitor\SDCopy
set MonitorRoot2=C:\SourceMonitor\GitCopy
set Mapping=HCMAPP_MonitorFolders_mapping.txt

cd C:\Python27
for /F "usebackq delims=; tokens=1,2,3,4" %%i in (%Mapping%) do (
Rem Sync latest source from Git and copy to C:\SourceMonitor
cd "%GitRoot%\%%j"
rem App\Resources
echo ====
git status
echo ====
echo ==============checkout %%j %%l branch =======================
echo ====
git checkout -f %%l
git pull


rem https://yangsu.github.io/pull-request-tutorial/
rem git checkout -b <new-branch-name> [<base-branch-name>]
rem git push -u origin <new-branch-name>

echo "%GitRoot%\%%j" "%MonitorRoot2%\%%j" %%k /S
robocopy "%GitRoot%\%%j" "%MonitorRoot2%\%%j" %%k /S

)


cd C:\Python27


del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Shared\Error.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Shared\ComingSoon.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Shared\_Layout.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Signup.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\ProvisioningProgressPartial.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Provisioning.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Legal.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Index.resx
del C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\SharedResource.resx
del C:\SourceMonitor\GitCopy\HCM\source\Packages\HumanCapitalManagementIntegration\Build\XRM\Solutions\HCMCommon\Components\Resources\en-US\resources.resx




rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Index.en-US.resx Index.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Legal.en-US.resx Legal.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Provisioning.en-US.resx Provisioning.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\ProvisioningProgressPartial.en-US.resx ProvisioningProgressPartial.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Home\Signup.en-US.resx Signup.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Shared\_Layout.en-US.resx _Layout.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Shared\ComingSoon.en-US.resx ComingSoon.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\Views\Shared\Error.en-US.resx Error.resx
rename C:\SourceMonitor\GitCopy\AOSPaas-landingService\Src\AosPaas.LandingService\Resources\SharedResource.en-US.resx SharedResource.resx


del C:\SourceMonitor\GitCopy\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Home\Index.resx
del C:\SourceMonitor\GitCopy\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Shared\Error.resx

del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\SharedResource.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\TenantOwner.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\SelectBapLocation.resx

del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Provisioning.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Legal.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Index.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Shared\__Layout.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Shared\Error.resx
del C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Shared\ComingSoon.resx

rename C:\SourceMonitor\GitCopy\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Home\Index.en-US.resx Index.resx
rename C:\SourceMonitor\GitCopy\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Shared\Error.en-US.resx Error.resx

rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\SharedResource.en-US.resx SharedResource.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\TenantOwner.en-US.resx TenantOwner.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\SelectBapLocation.en-US.resx SelectBapLocation.resx

rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Provisioning.en-US.resx Provisioning.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Legal.en-US.resx Legal.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Index.en-US.resx Index.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Shared\_Layout.en-US.resx _Layout.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Shared\Error.en-US.resx Error.resx
rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Shared\ComingSoon.en-US.resx ComingSoon.resx

rename C:\SourceMonitor\GitCopy\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\Signup.en-US.resx Signup.resx


rem the following path still need fixing
robocopy C:\Depots\MBSI\Projects\OOB\UI\Master\source\HCMApp_HCMFabric\Landing  C:\SourceMonitor\SDCopy\AOSPaas.landingService\Src\AosPaas.LandingService *.* /S


rem for mobile-app
robocopy C:\Depots\MBSI\Projects\D365App\UI\Master\Source\mobile-app C:\SourceMonitor\SDCopy\mobile-app\src\localization\messages *.* /S

rem for Shell UI files:
robocopy C:\Depots\MBSI\Projects\D365Shell\UI\Master\Source\Portal\lcl\App\Resources C:\SourceMonitor\SDCopy\Dynamics365-Dynamics365-Portal\src\Portal\App\Resources *.* /S
echo Y|copy C:\Depots\MBSI\Projects\D365Shell\UI\Master\Source\Portal\lcl\ServerResources.resx C:\SourceMonitor\SDCopy\Dynamics365-Dynamics365-Portal\src\Portal\ServerResources.resx


cd C:\Python27
for /F "usebackq delims=; tokens=1,2,3,4" %%i in (%Mapping%) do (
cd "%SDRoot%\%%i"
sd sync ...
)

rem robocopy "%SDRoot%\%%i" "%MonitorRoot1%\%%j" %%k /S
rem copy sd files to git folder structure to C:\SourceMonitor\SDCopy
rem need to udpate CopySDfilesToGitFolderstructure.py, as it only copy hcm files by hcm eol
cd C:\Python27
python SD2Git.py


FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set filelist=%%j%%k%%l
cd C:\GitProjects
dir *_en-US.xml /b/s >%filelist%.txt
echo y|copy C:\Gitprojects\%filelist%.txt C:\SourceMonitor\GitCopy\%filelist%.txt

echo y|copy C:\Gitprojects\%filelist%.txt C:\SourceMonitor\%filelist%.txt

rem for mobile-app
robocopy C:\Depots\MBSI\Projects\D365App\UI\Master\Source\mobile-app C:\SourceMonitor\SDCopy\mobile-app\src\localization\messages *.* /S

rem for Shell UI files:
robocopy C:\Depots\MBSI\Projects\D365Shell\UI\Master\Source\Portal\lcl\App\Resources C:\SourceMonitor\SDCopy\Dynamics365-Dynamics365-Portal\src\Portal\App\Resources *.* /S
echo Y|copy C:\Depots\MBSI\Projects\D365Shell\UI\Master\Source\Portal\lcl\ServerResources.resx C:\SourceMonitor\SDCopy\Dynamics365-Dynamics365-Portal\src\Portal\ServerResources.resx

echo F|xcopy C:\Gitprojects\HCM\source\Packages\HumanCapitalManagementIntegration\Build\XRM\Solutions\HCMCommon\Components\Resources\en-US\resources.en-US.resx C:\SourceMonitor\GitCopy\HCM\source\Packages\HumanCapitalManagementIntegration\Build\XRM\Solutions\HCMCommon\Components\Resources\en-US\resources.resx
rem for AOSPaas.landingService: rename source file names for AOSPaas.landingService

