@ECHO OFF

SETLOCAL
SET SCRIPTPATH=%~dp0
SET NUGETCREDENTIALPROVIDERBUNDLEDIR=%SCRIPTPATH%CredentialProviderBundle
SET NUGETEXE=%NUGETCREDENTIALPROVIDERBUNDLEDIR%\NuGet.exe
SET NUGETPACKAGEINSTALLDIR=%SCRIPTPATH%NuGetPackages
SET NUGETPACKAGESTOINSTALL=Microsoft.Dynamics.AX.HCMProd.Translations,Microsoft.Dynamics.AX.ApplicationCommonProd.Translations,Microsoft.Dynamics.AX.ApplicationIntegrationProd.Translations,Microsoft.Dynamics.AX.AccountingFoundationProd.Translations,Microsoft.Dynamics.AX.ElectronicReportingProd.Translations
SET RETAINEXISTINGINSTALLS=

IF /I "%~1" == "-RetainExistingInstalls" (
    SET RETAINEXISTINGINSTALLS=true
)

IF NOT EXIST "%NUGETEXE%" (
    ECHO.
    ECHO Could not find "%NUGETEXE%".
    ECHO.
    ECHO Please perform the following steps:
    ECHO   1.^) Navigate to https://msdyneng.visualstudio.com/AX%%20Application/_packaging?feed=AXApplication-Rel^&_a=feed
    ECHO   2.^) Click on the "Connect to feed" button
    ECHO   3.^) Click on the "Download NuGet + VSTS Credential Provider" link to download the latest
    ECHO       CredentialProviderBundle.zip file.
    ECHO   4.^) Extract the contents of the zip file to "%NUGETCREDENTIALPROVIDERBUNDLEDIR%".
    ECHO   5.^) Re-run this script file
    ECHO.
) ELSE (
    IF DEFINED RETAINEXISTINGINSTALLS (
        ECHO.
        ECHO Retaining existing installs under "%NUGETPACKAGEINSTALLDIR%"
        ECHO.
    ) ELSE (
        ECHO.
        ECHO Deleting existing installs under "%NUGETPACKAGEINSTALLDIR%"
        rd /s /q "%NUGETPACKAGEINSTALLDIR%"
        ECHO.
    )
    
    IF NOT EXIST "%NUGETPACKAGEINSTALLDIR%" ( md "%NUGETPACKAGEINSTALLDIR%" )


        ECHO.
        ECHO ####################################################################################################
        ECHO # Begin installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO."%NUGETEXE%" install Microsoft.Dynamics.AX.ApplicationCommonProd.Translations -Version 8.1.1108 -Source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -OutputDirectory "%NUGETPACKAGEINSTALLDIR%" -NonInteractive -DirectDownload
        ECHO.
        ECHO ####################################################################################################
        ECHO # Finished installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO.
        ECHO.


        ECHO.
        ECHO ####################################################################################################
        ECHO # Begin installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO."%NUGETEXE%" install Microsoft.Dynamics.AX.CostAccountingProd.Translations -Version 8.1.6 -Source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -OutputDirectory "%NUGETPACKAGEINSTALLDIR%" -NonInteractive -DirectDownload
        ECHO.
        ECHO ####################################################################################################
        ECHO # Finished installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO.
        ECHO.


        ECHO.
        ECHO ####################################################################################################
        ECHO # Begin installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO."%NUGETEXE%" install Microsoft.Dynamics.AX.AccountingFoundationProd.Translations -Version 8.1.1122 -Source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -OutputDirectory "%NUGETPACKAGEINSTALLDIR%" -NonInteractive -DirectDownload
        ECHO.
        ECHO ####################################################################################################
        ECHO # Finished installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO.
        ECHO.


        ECHO.
        ECHO ####################################################################################################
        ECHO # Begin installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO."%NUGETEXE%" install Microsoft.Dynamics.AX.ElectronicReportingProd.Translations -Version 8.1.2005 -Source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -OutputDirectory "%NUGETPACKAGEINSTALLDIR%" -NonInteractive -DirectDownload
        ECHO.
        ECHO ####################################################################################################
        ECHO # Finished installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO.
        ECHO.


        ECHO.
        ECHO ####################################################################################################
        ECHO # Begin installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        "%NUGETEXE%" install Microsoft.Dynamics.AX.HCMProd.Translations -Version 8.1.2009-rainmain0016 -Source https://msdyneng.pkgs.visualstudio.com/_packaging/AXApplication-Rel/nuget/v3/index.json -OutputDirectory "%NUGETPACKAGEINSTALLDIR%" -NonInteractive -DirectDownload
        ECHO.
        ECHO ####################################################################################################
        ECHO # Finished installing latest NuGet package for: %%i
        ECHO ####################################################################################################
        ECHO.
        ECHO.
        ECHO.


    ECHO.
    ECHO ####################################################################################################
    ECHO # Installed Packages
    ECHO ####################################################################################################
    ECHO.
    dir /b "%NUGETPACKAGEINSTALLDIR%"
    ECHO.
    ECHO.
)

:END
ENDLOCAL


cd C:\Python27
python HCM_DownloadPackages_v2.py