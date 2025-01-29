UsoClient ScanInstallWait 
wuauclt / detectnow / updatenow 
cleanmgr /sagerun
del %temp%\*.* /s /q /f
del C:\Windows\prefetch\*.*/s /q /f
ipconfig/flushDNS
%windir%\system32\rundll32.exe advapi32.dll, ProcessIdleTasks
REM sfc /scannow --> verifie intégrité système
REM chkdsk c: /f --> corrige erreur lecteur
REM defrag c: --> defragmente le lecteur
