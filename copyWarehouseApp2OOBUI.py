import shutil, os
langs=["zh-Hans","ar","cs","da","de","de-AT","de-CH","en-AU","en-CA","en-GB","en-IE","en-IN","en-MY","en-NZ","en-SG","en-ZA","es","es-MX","et","fi","fr","fr-BE","fr-CA","fr-CH","hu","is","it","it-CH","ja","lt","lv","nb-NO","nl","nl-BE","pl","pt-BR","ru","sv","th","tr"]


#Copy from 
#C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI\ar\AppResources.en-US.resx.lcl
#C:\Depots\MBSI\Projects\OOB\WarehouseMobileApp\UI\ar\DemoDataResources.en-US.resx.lcl
#copy to:
#C:\Depots\MBSI\Projects\OOB\UI\ar\WarehouseMobileApp\AppResources.en-US.resx.lcl
#C:\Depots\MBSI\Projects\OOB\UI\ar\WarehouseMobileApp\DemoDataResources.en-US.resx.lcl
OOBRoot='C:\\Depots\\MBSI\\Projects\\OOB\\UI\\test'

for lang in langs:
    print(lang)
    
    #target folder of the *.en-US.label.txt.lcl file
    PathTarget=os.path.join(OOBRoot,lang,'WarehouseMobileApp')
    if not os.path.exists(PathTarget):
    	os.makedirs(PathTarget)
    shutil.copy2(os.path.join('C:\\Depots\\MBSI\\Projects\\OOB\\WarehouseMobileApp\\UI',lang,'AppResources.en-US.resx.lcl'),os.path.join(PathTarget,'AppResources.en-US.resx.lcl'))
    shutil.copy2(os.path.join('C:\\Depots\\MBSI\\Projects\\OOB\\WarehouseMobileApp\\UI',lang,'DemoDataResources.en-US.resx.lcl'),os.path.join(PathTarget,'DemoDataResources.en-US.resx.lcl'))

