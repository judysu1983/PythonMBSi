  @ECHO OFF



  SET SCRIPTPATH=%~dp0
echo %CopytoDir%
  SET  CopytoDir=%SCRIPTPATH%RCS\UI

  SET  RCSLCLFiles=ar,ar-AE,cs,da,de,de-AT,de-CH,en-AU,en-CA,en-GB,en-IE,en-IN,en-MY,en-NZ,en-SG,en-ZA,es,es-MX,et,fi,fr,fr-BE,fr-CA,fr-CH,hu,is,it,it-CH,ja,lt,lv,nb-NO,nl,nl-BE,pl,pt-BR,ru,sv,th,tr,zh-Hans

    IF NOT EXIST "%CopytoDir%" ( md "%CopytoDir%" )

    FOR %%i in (%RCSLCLFiles%) DO (

  echo f|xcopy C:\Depots\MBSI\Projects\AX\RCS\UI\%%i\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\TenantOwner.en-US.resx.lcl C:\test\rcs\UI\%%i\RCS\ElectronicReporting-LandingService\TenantOwner.resx.lcl
   echo f|xcopy C:\Depots\MBSI\Projects\AX\RCS\UI\%%i\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\SelectBapLocation.en-US.resx.lcl C:\test\rcs\UI\%%i\RCS\ElectronicReporting-LandingService\SelectBapLocation.resx.lcl
   echo f|xcopy C:\Depots\MBSI\Projects\AX\RCS\UI\%%i\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\SharedResource.en-US.resx.lcl C:\test\rcs\UI\%%i\RCS\ElectronicReporting-LandingService\SharedResource.resx.lcl

   echo f|xcopy C:\Depots\MBSI\Projects\AX\RCS\UI\%%i\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Shared\Error.en-US.resx.lcl C:\test\rcs\UI\%%i\RCS\AosPaas-MarketingService\Error.resx.lcl
    echo f|xcopy C:\Depots\MBSI\Projects\AX\RCS\UI\%%i\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Home\Index.en-US.resx.lcl C:\test\rcs\UI\%%i\RCS\AosPaas-MarketingService\Index.resx.lcl


    )

  pause