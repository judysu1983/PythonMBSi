cd C:\Tools\CTAS2.2
rem HCMApp and HCMFabric
TaskEngine @C:\Depots\MBSI\Projects\OOB\UI\OOBApps_BI.arg -scenario:DailyWC -culture:de

rem CDM
TaskEngine @C:\Depots\MBSI\Projects\CDM\UI\CDM_UI_BI.arg -scenario:DailyWC -culture:de

rem D365_OOB_mobile-app
rem TaskEngine @C:\Depots\MBSI\Projects\D365App\UI\D365App_UI_BI.arg -scenario:DailyWC -culture:de
rem D365_OOB_OfficeApp
rem TaskEngine @C:\Depots\MBSI\Projects\AX\7.x_OfficeApps\UI\AX7.x_OfficeApp_UI_BI.arg -scenario:DailyWC -culture:de
rem shell UI
rem TaskEngine @C:\Depots\MBSI\Projects\D365Shell\UI\D365Shell_UI_BI.arg -scenario:DailyWC -culture:de
