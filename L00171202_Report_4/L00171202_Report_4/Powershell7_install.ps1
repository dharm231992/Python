mkdir "C:\Powershell7"
Set-Location C:\Powershell7
$URI = "https://aka.ms/install-powershell.ps1"
Invoke-RestMethod -Uri https://aka.ms/install-powershell.ps1 | 
Out-File -FilePath C:\Powershell7\Powershell7_install.ps1

