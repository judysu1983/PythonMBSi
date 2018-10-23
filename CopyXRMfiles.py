import os, shutil, stat, sys
langs=["ar", "bg", "ca-ES", "cs", "da", "de", "el", "es", "et", "eu", "fi", "fr", "gl", "he", "hi", "hr-HR", "hu", "id", "it", "ja", "kk", "ko", "lt", "lv", "ms-MY", "nb-NO", "nl", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sl", "sr-Cyrl-RS", "sr-Latn-RS", "sv", "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant", "zh-HK"]
langs2=["ar-SA", "bg-BG", "ca-ES", "cs-CZ", "da-DK", "de-DE", "el-GR", "es-ES", "et-EE", "eu-ES", "fi-FI", "fr-FR", "gl-ES", "he-IL", "hi-IN", "hr-HR", "hu-HU", "id-ID", "it-IT", "ja-JP", "kk-KZ", "ko-KR", "lt-LT", "lv-LV", "ms-MY", "nb-NO", "nl-NL", "pl-PL", "pt-BR", "pt-PT", "ro-RO", "ru-RU", "sk-SK", "sl-SI", "sr-Cyrl-RS", "sr-Latn-RS", "sv-SE", "th-TH", "tr-TR", "uk-UA", "vi-VN", "zh-CN", "zh-TW", "zh-HK"]

def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
#copy from C:\CTAS\OOBAPPs\runs\20180328-204222-m47pt9qfp7\work\GeneratedPackage\HCM\source\Packages\HumanCapitalManagementIntegration\Build\XRMSolutions\HCMCommon\Components\Resources\ar\resources.ar.resx
#to C:\test\XRMHB\HCM\source\Packages\HumanCapitalManagementIntegration\Build\XRMSolutions\HCMCommon\Components\Resources\ar-SA\resources.ar-SA.resx

CTASpath=r'C:\CTAS\OOBAPPs\runs\20181011-161757-x87dnnq5a4\work\GeneratedPackage'
Testroot=r'C:\test\XRMHB'
gitpath='HCM\source\Packages\HumanCapitalManagementIntegration\Build\XRM\Solutions\HCMCommon\Components\Resources'
def removefiles():
    targetFolder=os.path.join(Testroot,gitpath)
    for l in langs2:
        targetFile=os.path.join(targetFolder,l,'resources.'+l+'.resx')
        if os.path.isfile(targetFile):
            print('remove: '+targetFile)
            os.remove(targetFile)

def copyresx():
    i=0
    for lang in langs:
        LocalizedBinPath=os.path.join(CTASpath,gitpath)
        if os.path.exists(os.path.join(LocalizedBinPath,lang)):                
            #copy from C:\Depots\MBSI\Projects\OOB\UI\bg\TalentEngagement\Dynamics365-HCM-AppsPortalClient\messages.bg.xlf
            #to C:\test\TalentEngagement\Dynamics365-HCM-AppsPortalClient\localization\messages.bg-BG.xlf
            f='resources.'+lang+'.resx'
            #print(f)
            resxfile=os.path.join(LocalizedBinPath,lang,f)
            dst=os.path.join(Testroot,gitpath,langs2[i])
            f2='resources.'+langs2[i]+'.resx'
            i=i+1
            print(resxfile)
            print('Copy to: '+dst)

            if not os.path.exists(dst):
                    os.makedirs(dst)
            if os.path.exists(resxfile):
                    shutil.copy2(resxfile,os.path.join(dst,f2))

#removefiles()
copyresx()
