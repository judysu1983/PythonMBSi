
rem FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set clonefolder=%%j%%k%%l_App80

set clonefolder=App81

cd C:\test
md %clonefolder%

cd C:\test\%clonefolder%


cd C:\test\%clonefolder%
git clone "https://msdyneng.visualstudio.com/AX%%20Application/_git/ElectronicReporting"
cd ElectronicReporting
git checkout -f master
git pull


cd C:\test\%clonefolder%
git clone "https://msdyneng.visualstudio.com/AX%%20Application/_git/ApplicationCommon"
cd ApplicationCommon
git checkout -f master
git pull

cd C:\test\%clonefolder%
git clone "https://msdyneng.visualstudio.com/AX%%20Application/_git/Accounting%%20Foundation"
cd "Accounting%%20Foundation"
git checkout -f master
git pull

cd C:\test\%clonefolder%
git clone "https://msdyneng.visualstudio.com/AX%%20Application/AX%%20Application%%20Team/_git/Cost%%20Accounting"
cd "Cost%%20Accounting"
git checkout -f master
git pull

cd C:\test\%clonefolder%
git clone "https://msdyneng.visualstudio.com/AX%%20Application/_git/HCM"
cd HCM
git checkout -f rainmain
git pull
