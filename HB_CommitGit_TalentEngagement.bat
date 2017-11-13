@echo off

set GitRoot=C:\GitProjects

set Mapping=HB_CommitGit_TalentEngagement.txt

FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set HBdate=%%j%%k%%l
echo %HBdate%


rem "C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\test\HCMHB\source\Translation" "C:\GitProjects\HCM\source\Translation"

for /F "usebackq delims=; tokens=1,2,3" %%a in (%Mapping%) do (
cd "%GitRoot%\%%a"
git status
git checkout -f %%b
git pull
rem https://yangsu.github.io/pull-request-tutorial/
git checkout -b v-judysu/loc_%HBdate%
rem to acquire the token



echo #############copy over udpated files############
rem copy LCL files for HCM project
cd C:\Python27 
python copyTalentEngagement_v3.py %%a


attrib -r %GitRoot%\%%a\localization\*.* /s
cd "%GitRoot%\%%a"
rem sync latest strings before creating PR
rem npm install
npm install -g vsts-npm-auth --registry https://registry.npmjs.com --always-auth false
vsts-npm-auth -config .npmrc
npm run localization:extract 

git add .
git status


git commit -m "Localization Updates"
git push -u origin v-judysu/loc_%HBdate%
rem git push -u origin <new-branch-name>

)

rem "C:\Program Files\Beyond Compare 4\Bcompare.exe" "C:\CTAS\OOBAPPs\runs" "C:\GitProjects"

pause