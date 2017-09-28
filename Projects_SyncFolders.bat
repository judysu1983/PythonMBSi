@echo off
rem sync sd

set SDRoot=C:\Depots\MBSI\Projects
set Mapping=Project_SyncFolders.txt

cd C:\Python27
for /F "usebackq delims=; tokens=1,2,3,4" %%i in (%Mapping%) do (
cd "%SDRoot%\%%i"
sd sync ...
)


rem https://www.programcreek.com/python/example/71746/win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES
rem while running....