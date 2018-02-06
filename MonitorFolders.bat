Rem Start MonitorFolder app to monitor if there's any changes in the following folder
rem C:\GitProjects\OfficeApps\src\Apps
Rem Sync git or SD or TFS
Rem fileWatcher report if there's any changes and print it to a list, also report if there's no changes at all.
Rem done with monitor the current folder and start to monitor the next folder
python C:\Python27\MonitorFolders.py
cd C:\GitProjects\OfficeApps
git status
git fetch
git pull