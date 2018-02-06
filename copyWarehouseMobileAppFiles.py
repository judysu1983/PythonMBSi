import shutil, os
files=["AppResources","DemoDataResources"]
langs=["zh-Hant", "ar", "bg", "ca-ES", "cs", "da", "de", "de-AT", "de-CH", "el", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-US", "en-ZA", "es", "es-MX", "et", "eu", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "gl", "hi", "hr-HR", "hu", "id", "is", "it", "it-CH", "ja", "kk", "ko", "lt", "lv", "ms-MY", "nb-NO", "nl", "nl-BE", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sl", "sr-Cyrl-RS", "sr-Latn-RS", "sv", "th", "tr", "uk", "vi", "zh-Hans"]
#langs=['master']
AX7path=r'C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI'
AppPath=r'C:\Depots\MBSI\Projects\OOB\UI'


####copy UI files#####
# copy from C:\Depots\MBSI\Projects\AX\7.x\UI\en-AU\Application\f.resources.dll.lcl
# copy to    C:\Depots\MBSI\Projects\OOB\UI\en-AU\HcmApp\f.en-US.label.txt.lcl
for lang in langs:

   for f1 in files:
       dllf1=f1+".en-US.resx.lcl"
       labelf1=f1+".en-US.resx.lcl"
       print(os.path.join(AX7path,lang,dllf1))
       if os.path.isfile(os.path.join(AX7path,lang,dllf1)):

           if not os.path.exists(os.path.join(AppPath,lang,'WarehouseMobileApp')):
               os.makedirs(os.path.join(AppPath,lang,'WarehouseMobileApp'))
           shutil.copy2(os.path.join(AX7path,lang,dllf1),os.path.join(AppPath,lang,'WarehouseMobileApp',labelf1))



