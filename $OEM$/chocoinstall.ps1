
        $ErrorActionPreference = 'Stop'

function Install-Chocolatey {

    try {
        # Set TLS 1.2 (3072) as that is the minimum required by Chocolatey.org
        # Use integers because the enumeration value for TLS 1.2 won't exist
        # in .NET 4.0, even though they are addressable if .NET 4.5+ is
        # installed (.NET 4.5 is an in-place upgrade).
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
    } catch {
        Write-Warning $_.Exception.Message
        Write-Warning 'Unable to set PowerShell to use TLS 1.2. This is required for contacting Chocolatey as of 03 FEB 2020. https://chocolatey.org/blog/remove-support-for-old-tls-versions. If you see underlying connection closed or trust errors, you may need to do one or more of the following: (1) upgrade to .NET Framework 4.5+ and PowerShell v3+, (2) Call [System.Net.ServicePointManager]::SecurityProtocol = 3072; in PowerShell prior to attempting installation, (3) specify internal Chocolatey package location (set $env:chocolateyDownloadUrl prior to install or host the package internally), (4) use the Download + PowerShell method of install. See https://chocolatey.org/docs/installation for all install options.'
    }

    # Chocolatey is used to install softwares.
    $installationScriptBlock = [Scriptblock]::Create((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
    Invoke-Command -ScriptBlock $installationScriptBlock

    choco feature disable --name "showDownloadProgress"
    choco feature enable --name "allowGlobalConfirmation"
    
}
        
        Invoke-WebRequest -Uri "https://github.com/microsoft/winget-cli/releases/download/v1.1.12653/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle" -OutFile "C:\PS\WinGet.msixbundle"
Add-AppxPackage "C:\PS\WinGet.msixbundle"
        
        Invoke-WebRequest -Uri "https://github.com/microsoft/winget-cli/releases/download/v1.1.12653/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle" -OutFile "C:\PS\WinGet.msixbundle"
Add-AppxPackage "C:\PS\WinGet.msixbundle"
        
winget install 9WZDNCRFJ3TJ --accept-package-agreements --accept-source-agreements
choco install oracle-sql-developer -y
winget install Ubisoft.Connect --accept-package-agreements --accept-source-agreements
