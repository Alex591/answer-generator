


import shutil
import os

class Program:
    """
    Describes a program to be installed
    """
    programname:str
    __packageman:str|None
    __installflags:str|None
    installstring:str
    __winget:bool

    def __init__(self,programname):
        self.__winget=False
        self.programname=programname
        self.__packageman=None
        self.__installflags=None
        self.programname=self.fixlines(self.programname)
        self.programnamed= self.determineprogramname(self.programname)
        self.determineinstallflags()

        self.installstring=f"{'winget' if self.winget else 'choco'} install {self.programnamed} {self.__installflags}"

    def __str__(self):
        return f"Program: {self.programnamed} uses winget:{self.__winget}"
        
    def fixlines(self,old:str)->str:
        return old.replace("1","-")
    
    def determineprogramname(self,program:str)->str:
        wingetdict={"instagram":"9NBLGGH5L9XT","whatsapp":"9NKSQGP7F2NH","netflix":"9WZDNCRFJ3TJ","disneyplus":"9NXQXXLFST89",
        "spotify":"Spotify.Spotify","ubisoft-connect":"Ubisoft.Connect","steam":"Valve.Steam","origin":"ElectronicArts.EADesktop",
        "epicgameslauncher":"EpicGames.EpicGamesLauncher","winrar":"RARLab.WinRAR","itunes":"Apple.iTunes","vlc":"VideoLAN.VLC",
        "plex":"Plex.Plex","powertoys":"Microsoft.PowerToys","office":"Microsoft.Office"}
        if program in wingetdict.keys():
            self.__winget=True
            print(wingetdict[program])
            return wingetdict[program]
        else:
            return program



    def determineinstallflags(self)->None:
        self.__installflags="--accept-package-agreements --accept-source-agreements" if self.winget else "-y"
    @property
    def packageman(self)->str:
        return self.__packageman
    @property
    def installflag(self)->str:
        return self.__installflags
    @property
    def winget(self):
        return self.__winget



class PowershellScript():
    """
    Makes a Powershell Script that installs choco and optionally winget right at startup
    """
    def __init__(self):
        self.wingetrequired=False
        self.scriptbody=""
    

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
        return wingetinstall


def make_and_move(programs:list[Program]):
    """
    Function intended to be used by the UI to make the complete powershell script
    :param programs: a list of programs
    :return: None,this writes a powershell script to $OEM$\\$1
    """
    psscript=PowershellScript()
    psscript.scriptbody=psscript.scriptbody+psscript.installchoco()
    for x in programs:
        if x.winget:
            psscript.scriptbody=psscript.scriptbody+psscript.installwinget()

    for x in programs:
        psscript.scriptbody=psscript.scriptbody+"\n"+x.installstring
    with open("chocoinstall.ps1","w") as file:
        print(psscript.scriptbody,file=file)
    originaldir = os.path.join(os.getcwd(),"chocoinstall.ps1")
    destdir= os.path.join(os.getcwd(),"$OEM$","chocoinstall.ps1")
    shutil.move(originaldir,destdir)


if __name__=="__main__":
    test=Program("netflix")
    test3=Program("ubisoft-connect")
    test2=Program("oracle1sql1developer")
    print(test.installstring)
    make_and_move([test,test2,test3])