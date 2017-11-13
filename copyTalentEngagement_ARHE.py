import os, shutil, stat
SDpath=r'C:\Depots\MBSI\Projects\OOB\UI'

def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

GitPath=r'C:\test\Ttt'

if os.path.exists(GitPath):
    shutil.rmtree(GitPath, onerror=del_rw)
os.makedirs(GitPath)

langs=["ar","he"]
langs2=["ar-SA", "he-IL"]

components=["Dynamics365-HCM-OnboardingClient","Dynamics365-HCM-MsAssessClient","Dynamics365-HCM-Offermanagement","Dynamics365-HCM-TalentEngagement","Dynamics365-HCM-AppsPortalClient"]	
def copymessages():
        for lang in langs:
                for com in components:
                        if os.path.exists(os.path.join(SDpath,lang)):
                                #copy from C:\Depots\MBSI\Projects\OOB\UI\bg\TalentEngagement\Dynamics365-HCM-AppsPortalClient\messages.bg.xlf
                                #to C:\test\TalentEngagement\Dynamics365-HCM-AppsPortalClient\localization\messages.bg-BG.xlf
                                f='messages.'+lang+'.xlf'
                                #print(f)
                                sdfile=os.path.join(SDpath,lang,'TalentEngagement',com,f)
                                dst=os.path.join(GitPath,com,'localization')
                                print(sdfile)
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
                for i in range(2):
                        f='messages.'+langs[i]+'.xlf'
                        f2='messages.'+langs2[i]+'.xlf'

                        src=os.path.join(GitPath,com,'localization',f)
                        dst=os.path.join(GitPath,com,'localization',f2)
                        #print('from '+src)
                        #print('to '+dst)
                        if not os.path.exists(dst):
                                os.rename(src,dst)
copymessages()
renameMessages()

