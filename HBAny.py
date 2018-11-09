import sys, os, datetime
print(sys.argv)
if len(sys.argv)>1:
    reponame=''.join(sys.argv[1])
    branchname=''.join(sys.argv[2])
now=datetime.datetime.now()
mybranch='v-judysu/loc_'+now.strftime("%Y%m%d%H%M")    
os.chdir(r'C:\Gitprojects\%s' % reponame)
os.system(r'git checkout -f %s' % branchname )
os.system(r'git pull')

#checkout my branch and commit
os.system(r'git checkout -b %s' % mybranch)
input("Copy over the updated files,Press Enter...")

os.system(r'git add .')
os.system(r'git status')
os.system(r'git commit -m "Localiation Updates"')
os.system(r'git push -u origin %s' % mybranch)
