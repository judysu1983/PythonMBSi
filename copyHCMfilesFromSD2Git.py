import os, shutil, stat
# copy from C:\Depots\MBSI\Projects\OOB\UI\ar\HcmApp\*.lcl
# to C:\GitProjects\HCM\source\Translation\LCL\ar\*.lcl
SDpath=r'C:\Depots\MBSI\Projects\OOB\UI'
GitPath=r'C:\test\HCMHB\source\Translation\LCL'
#langs=["zh-Hant", "ar", "bg", "ca-ES", "cs", "da", "de", "de-AT", "de-CH", "el", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-US", "en-ZA", "es", "es-MX", "et", "eu", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "gl", "hi", "hr-HR", "hu", "id", "is", "it", "it-CH", "ja", "kk", "ko", "lt", "lv", "ms-MY", "nb-NO", "nl", "nl-BE", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sl", "sr-Cyrl-RS", "sr-Latn-RS", "sv", "th", "tr", "uk", "vi", "zh-Hans"]
langs=["zh-HK", "ar", "bg", "ca-ES", "cs", "da", "de", "de-AT", "de-CH", "el", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-US", "en-ZA", "es", "es-MX", "et", "eu", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "gl", "hi", "hr-HR", "hu", "id", "is", "it", "it-CH", "ja", "kk", "ko", "lt", "lv", "Master", "ms-MY", "nb-NO", "nl", "nl-BE", "pl", "pt", "pt-BR", "pt-PT", "ro", "ru", "sk", "sl", "sr-Cyrl-RS", "sr-Latn-RS", "sv", "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant"]


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

#remove all the files under C:\SourceMonitor\SDCopy    
if os.path.exists(GitPath):
    shutil.rmtree(GitPath, onerror=del_rw)
os.makedirs(GitPath)

for lang in langs:
        print('copy LCL for: '+lang)
        if os.path.exists(os.path.join(SDpath,lang,'HcmApp')):
                shutil.copytree(os.path.join(SDpath,lang,'HcmApp'),os.path.join(GitPath,lang))
