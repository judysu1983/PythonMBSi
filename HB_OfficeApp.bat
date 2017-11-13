cd C:\Tools\CTAS2.2
rem HCMApp and HCMFabric
TaskEngine @C:\Depots\MBSI\Projects\AX\7.x_OfficeApps\UI\AX7.x_OfficeApp_UI.arg -scenario:WeeklyHandback -culture:ar;cs;da;de;es;et;fi;fr;hu;is;it;ja;lt;lv;nb-NO;nl;pl;pt-BR;ru;sv;th;tr;zh-Hans;nl-BE;fr-BE;fr-CA;fr-CH;de-AT;de-CH;es-MX;it-CH;en-AU;en-CA;en-GB;en-IE;en-MY;en-NZ;en-SG;en-ZA;en-IN;eu;bg;ca-ES;zh-HANT;hr-HR;gl;el;hi;id;kk;ko;ms-MY;pt-PT;ro;sr-Cyrl-RS;sr-Latn-RS;sk;sl;uk;vi



FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set HBdate=%%j%%k%%l
echo %HBdate%

cd "C:\Gitprojects\OfficeApps"
git status
git checkout -f master
git pull
git checkout -b v-judysu/loc_%HBdate%
echo #############copy over udpated files############
c:\Windows\explorer.exe "C:\CTAS\AX7.x_OfficeApp\runs"
c:\Windows\explorer.exe "C:\GitProjects"
"C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\CTAS\AX7.x_OfficeApp\runs" "C:\Gitprojects\OfficeApps"
pause

git add .
git status


git commit -m "Localization Updates"
git push -u origin v-judysu/loc_%HBdate%
