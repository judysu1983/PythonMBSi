import os, shutil
SDpath=r'C:\Depots\MBSI\Projects\OOB\UI'
GitPath=r'C:\test\TalentEngagement'
langs=["bg", "ca-ES", "cs", "da", "de", "de-AT", "de-CH", "el", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-ZA", "es", "es-MX", "et", "eu", "fi", "fr", "fr-BE", "fr-CA", "fr-CH", "gl", "hi", "hr-HR", "hu", "id", "is", "it", "it-CH", "ja", "kk", "ko", "lt", "lv", "ms-MY", "nb-NO", "nl", "nl-BE", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sl", "sr-Cyrl-RS", "sr-Latn-RS", "sv", "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant", "zh-HK"]
langs2=["bg-BG", "ca-ES", "cs-CZ", "da-DK", "de-DE", "de-AT", "de-CH", "el-GR", "en-AU", "en-CA", "en-GB", "en-IE", "en-IN", "en-MY", "en-NZ", "en-SG", "en-ZA", "es-ES", "es-MX", "et-EE", "eu-ES", "fi-FI", "fr-FR", "fr-BE", "fr-CA", "fr-CH", "gl-ES", "hi-IN", "hr-HR", "hu-HU", "id-ID", "is-is", "it-IT", "it-CH", "ja-JP", "kk-KZ", "ko-KR", "lt-LT", "lv-LV", "ms-MY", "nb-NO", "nl-NL", "nl-BE", "pl-PL", "pt-BR", "pt-PT", "ro-RO", "ru-RU", "sk-SK", "sl-SI", "sr-Cyrl-RS", "sr-Latn-RS", "sv-SE", "th-TH", "tr-TR", "uk-UA", "vi-VN", "zh-Hans-CN", "zh-Hant-TW", "zh-Hant-HK"]
##langs=["ar","he"]
##langs2=["ar-SG", "he-IL"]

components=["Dynamics365-HCM-TalentEngagement"]	
def copymessages():
        for lang in langs:
                for com in components:
                        if os.path.exists(os.path.join(SDpath,lang)):
                                #copy from C:\Depots\MBSI\Projects\OOB\UI\bg\TalentEngagement\Dynamics365-HCM-AppsPortalClient\messages.bg.xlf
                                #to C:\test\TalentEngagement\Dynamics365-HCM-AppsPortalClient\localization\messages.bg-BG.xlf
                                f='applicant_template_'+lang+'.xlsx'
                                print(f)
                                sdfile=os.path.join(SDpath,lang,'TalentEngagement',com,f)
                                dst=os.path.join(GitPath,com,'localization')
                                print(dst)
                                if not os.path.exists(dst):
                                        os.makedirs(dst)
                                if os.path.exists(sdfile):
                                        shutil.copy2(sdfile,os.path.join(dst,f))
                        
#### rename the files ####
# from C:\test\TalentEngagement\Dynamics365-HCM-MsAssessClient\localization\messages.bg.xlf to
# to C:\test\TalentEngagement\Dynamics365-HCM-MsAssessClient\localization\messages.bg-BG.xlf
def renameMessages():
        for com in components:
                for i in range(60):
                        f='applicant_template_'+langs[i]+'.xlsx'
                        f2='applicant_template_'+langs2[i]+'.xlsx'
                        print('rename from '+f+' to '+f2)

                        src=os.path.join(GitPath,com,'localization',f)
                        dst=os.path.join(GitPath,com,'localization',f2)
                        print('from '+src)
                        print('to '+dst)
                        if not os.path.exists(dst):
                                os.rename(src,dst)


copymessages()
renameMessages()

