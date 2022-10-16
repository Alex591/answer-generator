


from ast import Str


class Program:
    """
    Describes a program to be installed
    """
    programname:str
    packageman:str
    def __init__(self,programname):
        self.programname=programname
        self.__packageman=None
        self.__installflags=None
        self.programname=self.fixlines(self.programname)
        self.__winget=False
        
    def fixlines(self,old:str)->str:
        return old.replace("1","-")
    
    def determineprogramname(self,program:str)->str:
        wingetdict={"instagram":"9NBLGGH5L9XT","whatsapp":"9NKSQGP7F2NH","netflix":"9WZDNCRFJ3TJ","disneyplus":"9NXQXXLFST89",
        "spotify":"Spotify.Spotify","ubisoft-connect":"Ubisoft.Connect","steam":"Valve.Steam","origin":"ElectronicArts.EADesktop",
        "epicgameslauncher":"EpicGames.EpicGamesLauncher","winrar":"RARLab.WinRAR","itunes":"Apple.iTunes","vlc":"VideoLAN.VLC",
        "plex":"Plex.Plex","powertoys":"Microsoft.PowerToys"}
        if program in ["instagram","whatsapp","netflix","disneyplus"]:
            self.__winget=True
            if program=="instagram":
                return "9NBLGGH5L9XT"
            elif program=="whatsapp":
                return "9NKSQGP7F2NH"
            elif program=="netflix":
                return "9WZDNCRFJ3TJ"
            elif program == "disneyplus":
                return "9NXQXXLFST89"
       
        else:
            return program
    def determinepackageman()->str:
        




        pass


    def determineinstallflags()->str:
        pass
    @property
    def packageman(self)->str:
        return self.__packageman
    @property
    def installflag(self)->str:
        return self.__installflags



class PowershellScript():
    """
    Makes a Powershell Script that installs choco and optionally winget right at startup
    """
    def __init__(self):
        self.wingetrequired=False
    

    def installchoco(self)->str:
        chocoinstall="""
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
        """
        return chocoinstall
    def installwinget(self)->str:
        wingetinstall="""
        Invoke-WebRequest -Uri "https://github.com/microsoft/winget-cli/releases/download/v1.1.12653/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle" -OutFile "C:\PS\WinGet.msixbundle"
Add-AppxPackage "C:\PS\WinGet.msixbundle"
        """
