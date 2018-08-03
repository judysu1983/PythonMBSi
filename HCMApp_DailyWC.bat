cd C:\Tools\CTAS2.5
rem HCMApp and HCMFabric
TaskEngine @C:\Depots\MBSI\Projects\OOB\UI\BI_OOBApps.arg -scenario:DailyWC -culture:de

cd C:\Python27
python testEmail.py

rem CDM
rem TaskEngine @C:\Depots\MBSI\Projects\CDM\UI\BI_CDM_UI.arg -scenario:DailyWC -culture:de

rem D365_OOB_mobile-app
rem TaskEngine @C:\Depots\MBSI\Projects\D365App\UI\D365App_UI_BI.arg -scenario:DailyWC -culture:de
rem D365_OOB_OfficeApp
rem TaskEngine @C:\Depots\MBSI\Projects\AX\7.x_OfficeApps\UI\AX7.x_OfficeApp_UI_BI.arg -scenario:DailyWC -culture:de
rem shell UI
rem TaskEngine @C:\Depots\MBSI\Projects\D365Shell\UI\D365Shell_UI_BI.arg -scenario:DailyWC -culture:de
