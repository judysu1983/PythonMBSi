import shutil,os
#langs=['ar', 'cs', 'da', 'de', 'de-AT', 'de-CH', 'en-AU', 'en-CA', 'en-GB', 'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-SG', 'en-ZA', 'es', 'es-MX', 'et', 'fi', 'fr', 'fr-BE', 'fr-CA', 'fr-CH', 'hu', 'is', 'it', 'it-CH', 'ja', 'lt', 'lv', 'nb-NO', 'nl', 'nl-BE', 'pl', 'pt-BR', 'ru', 'sv', 'th', 'tr', 'zh-Hans']
langs=['ar', 'bg', 'ca', 'ca-ES', 'cs', 'da', 'de', 'de-AT', 'de-CH', 'el', 'en-AU', 'en-CA', 'en-GB', 'en-IE', 'en-IN', 'en-MY', 'en-NZ', 'en-SG', 'en-ZA', 'es', 'es-MX', 'et', 'eu', 'fi', 'fr', 'fr-BE', 'fr-CA', 'fr-CH', 'gl', 'he', 'hi', 'hr', 'hr-HR', 'hu', 'id', 'is', 'it', 'it-CH', 'ja', 'kk', 'ko', 'lt', 'lv', 'Master', 'ms', 'ms-MY', 'nb-NO', 'nl', 'nl-BE', 'pl', 'pt-BR', 'pt-PT', 'ro', 'ru', 'sk', 'sl', 'sr-Cyrl-RS', 'sr-Latn-RS', 'sv', 'th', 'tr', 'uk', 'vi', 'zh-Hans', 'zh-Hant']

#mobile app
# from : C:\Depots\MBSI\Projects\D365App\UI\ar\mobile-app\en-US.resjson.lcl
# to : C:\Depots\MBSI\Projects\OOB\UI\ar\mobile-app\src\localization\messages\en-US.resjson.lcl

#shell UI copied LCL

#office App - done
# from C:\Depots\MBSI\Projects\AX\7.x_OfficeApps\UI\de\OfficeApps\DynamicsAppResources.resjson.lcl
#to C:\Depots\MBSI\Projects\OOB\UI\de\OfficeApps\src\Apps\DynamicsAX.AppWeb\Resources\DynamicsAppResources.resjson.lcl


#from C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI\cs\AppResources.en-US.resx.lcl
#to C:\Depots\MBSI\Projects\OOB\UI\cs\WarehouseMobileApp\WarehouseMobileApp\WarehouseMobileApp\Resources\AppResources.resx.lcl
#from C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI\cs\DemoDataResources.en-US.resx.lcl
#to C:\Depots\MBSI\Projects\OOB\UI\cs\WarehouseMobileApp\WarehouseMobileApp.ServiceProxy.Demo\Resources\DemoDataResources.resx.lcl


OOBpath='C:\\Depots\\MBSI\\Projects\\OOB\\test3'
#OfficeAppPath='C:\\Depots\\MBSI\\Projects\\AX\\7.x_OfficeApps\\UI'
OfficeAppPath='C:\\Depots\\MBSI\\Projects\\D365App\\UI'
for lang in langs:
    if os.path.isfile(os.path.join(OfficeAppPath,lang,'mobile-app\\en-US.resjson.lcl')):
        os.makedirs(os.path.join(OOBpath,lang,'mobile-app\\src\\localization\\messages'))
        shutil.copy(os.path.join(OfficeAppPath,lang,'mobile-app\\en-US.resjson.lcl'),os.path.join(OOBpath,lang,'mobile-app\\src\\localization\\messages'))
        
##    if os.path.isfile(os.path.join(OfficeAppPath,lang,'AppResources.en-US.resx.lcl')):
##        os.makedirs(os.path.join(OOBpath,lang,'WarehouseMobileApp\\WarehouseMobileApp\\WarehouseMobileApp\\Resources'))
##        shutil.copy2(os.path.join(OfficeAppPath,lang,'AppResources.en-US.resx.lcl'),os.path.join(OOBpath,lang,'WarehouseMobileApp\\WarehouseMobileApp\\WarehouseMobileApp\\Resources\\AppResources.resx.lcl'))
##        os.makedirs(os.path.join(OOBpath,lang,'WarehouseMobileApp\\WarehouseMobileApp.ServiceProxy.Demo\\Resources'))
##        shutil.copy2(os.path.join(OfficeAppPath,lang,'DemoDataResources.en-US.resx.lcl'),os.path.join(OOBpath,lang,'WarehouseMobileApp\\WarehouseMobileApp.ServiceProxy.Demo\\Resources\\DemoDataResources.resx.lcl'))



##    if os.path.isfile(os.path.join(OfficeAppPath,lang,'OfficeApps\\DynamicsAppResources.resjson.lcl')):
##        #print os.path.join(OfficeAppPath,lang,'OfficeApps\\DynamicsAppResources.resjson.lcl')
##        os.makedirs(os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.AppWeb\\Resources'))
##        os.makedirs(os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.Common\\Resources'))
##        os.makedirs(os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.Outlook\\Resources'))
##        shutil.copy(os.path.join(OfficeAppPath,lang,'OfficeApps\\DynamicsAppResources.resjson.lcl'),os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.AppWeb\\Resources'))
##        shutil.copy(os.path.join(OfficeAppPath,lang,'OfficeApps\\PowerAppsResources.resjson.lcl'),os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.AppWeb\\Resources'))
##        shutil.copy(os.path.join(OfficeAppPath,lang,'OfficeApps\\OfficeAppResources.resjson.lcl'),os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.Common\\Resources'))
##        shutil.copy(os.path.join(OfficeAppPath,lang,'OfficeApps\\Resources.resjson.lcl'),os.path.join(OOBpath,lang,'OfficeApps\\src\\Apps\\DynamicsAX.Outlook\\Resources'))
    else:
        print(lang + ' does not apply.')


