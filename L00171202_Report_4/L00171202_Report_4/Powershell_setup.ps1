Get-Help -Name C:\Powershell7\Powershell7_install.ps1

$PARAMS = @{
 UseMsi = $true
 Quiet = $true
 AddExplorerContextMenu = $true
 EnablePSRemoting = $true
}
C:\Powershell\Powershell7_install.ps1 @PARAMS