@echo off

set GitRoot=C:\GitProjects

set Mapping=HB_CommitGit_CDM.txt

FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set HBdate=%%j%%k%%l
echo %HBdate%

rem copy LCL files for HCM project

rem "C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\test\HCMHB\source\Translation" "C:\GitProjects\HCM\source\Translation"

for /F "usebackq delims=; tokens=1,2,3" %%a in (%Mapping%) do (
cd "%GitRoot%\%%a"
git status
git checkout -f %%b
git pull
rem https://yangsu.github.io/pull-request-tutorial/
git checkout -b v-judysu/loc_%HBdate%

echo #############copy over udpated files############
pause

git add .
git status

pause
git commit -m "Localization Updates"
git push -u origin v-judysu/loc_%HBdate%
rem git push -u origin <new-branch-name>

)

rem "C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\CTAS\CDM\runs" "C:\GitProjects"

