@echo off

set GitRoot=C:\test\App73

set Mapping=HB_CommitGit_HCMAPP73.txt

FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set HBdate=%%j%%k%%l
echo %HBdate%


cd C:\Tools\CTAS2.4
rem Dynamics 365 HCM App – 
rem TaskEngine @C:\Depots\MBSI\Projects\OOB\UI\OOBApps.arg -scenario:WeeklyHandback -culture:ar;cs;da;de;es;et;fi;fr;hu;is;it;ja;lt;lv;nb-NO;nl;pl;pt-BR;ru;sv;th;tr;zh-Hans;nl-BE;fr-BE;fr-CA;fr-CH;de-AT;de-CH;es-MX;it-CH;en-AU;en-CA;en-GB;en-IE;en-MY;en-NZ;en-SG;en-ZA;en-IN
rem TaskEngine @C:\Depots\MBSI\Projects\OOB\UI\OOBApps_HCMFabric.arg -scenario:WeeklyHandback -culture:ar;cs;da;de;es;et;fi;fr;hu;is;it;ja;lt;lv;nb-NO;nl;pl;pt-BR;ru;sv;th;tr;zh-Hans;nl-BE;fr-BE;fr-CA;fr-CH;de-AT;de-CH;es-MX;it-CH;en-AU;en-CA;en-GB;en-IE;en-MY;en-NZ;en-SG;en-ZA;en-IN
rem c:\Windows\explorer.exe "C:\CTAS\OOBAPPs\runs"
rem c:\Windows\explorer.exe "C:\GitProjects"

rem copy LCL files for HCM project
cd C:\Python27 
rem python tmp_copyApp73HCMLCLfiles2Git.py


for /F "usebackq delims=; tokens=1,2,3" %%a in (%Mapping%) do (
	echo "%GitRoot%\%%a"
cd "%GitRoot%\%%a"
git status
git checkout -f %%b

git pull
rem https://yangsu.github.io/pull-request-tutorial/
git checkout -b v-judysu/loc_%HBdate%

echo #############copy over udpated files############
pause

git add *.lcl
git status


git commit -m "Localization Updates"
git push -u origin v-judysu/loc_%HBdate%
rem git push -u origin <new-branch-name>

)

rem "C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\test\HCMHB\source\Translation" "C:\GitProjects\HCM\source\Translation"
rem UserDefinedApp.en-US.label.txt*;Leave.en-US.label.txt*;PersonnelBusinessProcess.en-US.label.txt*

rem "C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\CTAS\OOBAPPs\runs" "C:\GitProjects"
rem ElectronicReportingMapping.*txt;ElectronicReporting.*txt;TaxEngine.*txt

