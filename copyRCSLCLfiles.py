import os, shutil,stat

#Copy files from C:\Depots\MBSI\Projects\AX\RCS\UI\pt-BR\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\TenantOwner.en-US.resx.lcl
##C:\Depots\MBSI\Projects\AX\RCS\UI\pt-BR\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\Views\Home\SelectBapLocation.en-US.resx.lcl
##C:\Depots\MBSI\Projects\AX\RCS\UI\pt-BR\ElectronicReporting-LandingService\src\AosPaas.LandingService\Resources\SharedResource.en-US.resx.lcl
##
##C:\Depots\MBSI\Projects\AX\RCS\UI\pt-BR\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Shared\Error.en-US.resx.lcl
##C:\Depots\MBSI\Projects\AX\RCS\UI\pt-BR\AosPaas-MarketingService\src\AosPaas.MarketingService\Resources\Views\Home\Index.en-US.resx.lcl

#C:\test\rcs\UI\pt-BR\RCS\ElectronicReporting-LandingService


langs=["ar","ar-AE","cs","da","de","de-AT","de-CH","en-AU","en-CA","en-GB","en-IE","en-IN","en-MY","en-NZ","en-SG","en-ZA","es","es-MX","et","fi","fr","fr-BE","fr-CA","fr-CH","hu","is","it","it-CH","ja","lt","lv","nb-NO","nl","nl-BE","pl","pt-BR","ru","sv","th","tr","zh-Hans"]
MarketingServicefiles=["src\AosPaas.MarketingService\Resources\Views\Shared\Error.en-US.resx.lcl","src\\AosPaas.MarketingService\\Resources\\Views\\Home\\Index.en-US.resx.lcl"]
LandingServicefiles=["src\AosPaas.LandingService\Resources\SharedResource.en-US.resx.lcl","src\AosPaas.LandingService\Resources\Views\Home\SelectBapLocation.en-US.resx.lcl","src\AosPaas.LandingService\Resources\Views\Home\TenantOwner.en-US.resx.lcl"]


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    
def copyLCL(Component,fileList):


    
    #remove all the files under C:\SourceMonitor\SDCopy    
##    if os.path.exists(copytoroot):
##        shutil.rmtree(copytoroot, onerror=del_rw)
##    os.makedirs(copytoroot)
    copytoroot=r'C:\test\RCS\UI'
    SDpath=r'C:\Depots\MBSI\Projects\AX\RCS\UI'
    for lang in langs:
        for f in fileList:
            #print('copy LCL for: '+lang+': '+f)
            sdpath=os.path.join(SDpath,lang,Component)
            print(sdpath)
            copytopath=os.path.join(copytoroot,lang,'RCS')
            print(copytopath)
            if not os.path.exists(copytopath):
                os.makedirs(copytopath)
            if os.path.exists(sdpath):
                print(os.path.join(copytopath,f))
                shutil.copy2(os.path.join(sdpath,f),os.path.join(copytopath,Component,f))


##
copyLCL('AosPaas-MarketingService',MarketingServicefiles)
copyLCL('ElectronicReporting-LandingService',LandingServicefiles)

