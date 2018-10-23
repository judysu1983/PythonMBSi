
rem FOR /F "tokens=1-4 delims=/- " %%i IN ('date/T') DO set clonefolder=%%j%%k%%l_App80

set clonefolder=App80_CU

cd C:\test
md %clonefolder%

cd C:\test\%clonefolder%

git clone "https://msdyneng.visualstudio.com/AX%%20Application/_git/ElectronicReporting"

cd ElectronicReporting
git checkout -f release/App80_CU
git pull

