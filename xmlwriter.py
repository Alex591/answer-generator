from xml.dom import minidom
from xml.etree import ElementTree as ET
import handler


class User():
    def __init__(self, role: str, username: str, password: str,wallpapers:list=[]):
        self.__role = role
        self.__username = username
        self.__password = password
        self.__wallpaper= wallpapers

    def convertpassword(self, password):
        pass

    @property
    def role(self):
        return self.__role

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.convertpassword(self.__password)


class PrivacySettings:
    pass


class Writer():
    def __init__(self):
        # root element
        self.root = ET.Element("unattend", {"xmlns": "urn:schemas-microsoft-com:unattend",
                                            "xmlns:wcm": "http://schemas.microsoft.com/WMIConfig/2002/State"})

        # Constants
        self.architecture = "amd64"

    # Helper functions

    def component(self, name: str) -> dict:
        """
        Since component declarations are largely the same (except the name), this function makes it easier to declare components
        :return: a dictionary containing the component name + constants
        """

        return {"name": f"{name}",
                "processorArchitecture": f"{self.architecture}",
                "publicKeyToken": "31bf3856ad364e35",
                "language": "neutral",
                "versionScope": "nonSxS"
                }

    def write(self, filename="autounattend.xml"):
        out = ET.tostring(self.root)
        dom = minidom.parseString(out)

        xml_str = dom.toprettyxml(encoding="utf-8", indent="\t")

        with open(filename, "wb") as f:
            f.write(xml_str)

    # Pass functions
    def add_win_pe_pass(self, setuplang: str = "en-US", inputlocale: list | None = None, systemlocale: str = "en-US",
                        userlocale: str = "hu-HU",
                        windowsedition: str = "Professional", fullname: str = "teszt_elek", organization: str = "",
                        virtual_machine: None | bool = None):
        if inputlocale is None:
            inputlocale = ["en-US"]
        pepass = ET.SubElement(self.root, "settings", {"pass": "windowsPE"})

        # adds winPE_Core component
        component_winpe = ET.SubElement(pepass, "component",
                                        self.component("Microsoft-Windows-International-Core-WinPE"))
        setupuilang = ET.SubElement(component_winpe, "SetupUILanguage")
        ET.SubElement(setupuilang, "UILanguage").text = setuplang
        if len(inputlocale) == 1:
            # https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-international-core-inputlocale
            ET.SubElement(component_winpe, "InputLocale").text = inputlocale[0]
        else:
            #         If multiple keyboard languages are needed, add them separated with commas
            tmp = "; ".join(inputlocale)
            ET.SubElement(component_winpe, "InputLocale").text = tmp
        ET.SubElement(component_winpe, "SystemLocale").text = systemlocale
        ET.SubElement(component_winpe, "UILanguage").text = setuplang
        ET.SubElement(component_winpe, "UserLocale").text = userlocale
        # adds WinPE_Windows_Setup
        component_winsetup = ET.SubElement(pepass, "component",
                                           self.component("Microsoft-Windows-Setup"))

        #This is requires to bypass the inital windows edition screen
        imageinstall=ET.SubElement(component_winsetup,"ImageInstall")
        osimage=ET.SubElement(imageinstall,"OSImage")
        installfrom=ET.SubElement(osimage,"InstallFrom")
        imagedetails=ET.SubElement(installfrom,"MetaData",{"wcm:action":"add"})
        ET.SubElement(imagedetails,"Key").text="/image/index"
        ET.SubElement(imagedetails,"Value").text="1"

        #setting the product key
        userdata = ET.SubElement(component_winsetup, "UserData")
        productkey = ET.SubElement(userdata, "ProductKey")
        ET.SubElement(productkey, "Key").text = handler.getproductkey(windowsedition)
        ET.SubElement(productkey, "WillShowUI").text = "Never"
        ET.SubElement(userdata, "AcceptEula").text = "true"
        ET.SubElement(userdata, "FullName").text = fullname
        ET.SubElement(userdata, "Organization").text = organization
        # Installing Windows 11 on a virtual machine requires some checks to be bypassed, namely: TPM, Secure Boot, Storage,CPU,Ram
        if virtual_machine is True:
            runsync = ET.SubElement(component_winsetup, "RunSynchronous")
            # Bypass TPM
            runcommand_tpmbypass = ET.SubElement(runsync, "RunSynchronousCommand", {"wcm:action": "add"})
            ET.SubElement(runcommand_tpmbypass, "Order").text = '1'
            ET.SubElement(runcommand_tpmbypass,
                          "Path").text = "reg add HKLM\System\Setup\LabConfig /v BypassTPMCheck /t reg_dword /d 0x00000001 /f"
            # Bypass Secure Boot
            runcommand_securebootbypass = ET.SubElement(runsync, "RunSynchronousCommand", {"wcm:action": "add"})
            ET.SubElement(runcommand_securebootbypass, "Order").text = '2'
            ET.SubElement(runcommand_securebootbypass,
                          "Path").text = "reg add HKLM\System\Setup\LabConfig /v BypassSecureBootCheck /t reg_dword /d 0x00000001 /f"
            # Bypass Storage requirements
            runcommand_storagebypass = ET.SubElement(runsync, "RunSynchronousCommand", {"wcm:action": "add"})
            ET.SubElement(runcommand_storagebypass, "Order").text = '3'
            ET.SubElement(runcommand_storagebypass,
                          "Path").text = "reg add HKLM\System\Setup\LabConfig /v BypassStorageCheck /t reg_dword /d 0x00000001 /f"
            # Bypass CPU requirements
            runcommand_cpubypass = ET.SubElement(runsync, "RunSynchronousCommand", {"wcm:action": "add"})
            ET.SubElement(runcommand_cpubypass, "Order").text = '4'
            ET.SubElement(runcommand_cpubypass,
                          "Path").text = "reg add HKLM\System\Setup\LabConfig /v BypassCPUCheck /t reg_dword /d 0x00000001 /f"
            # Bypass RAM Check
            runcommand_rambypass = ET.SubElement(runsync, "RunSynchronousCommand", {"wcm:action": "add"})
            ET.SubElement(runcommand_rambypass, "Order").text = '5'
            ET.SubElement(runcommand_rambypass,
                          "Path").text = "reg add HKLM\System\Setup\LabConfig /v BypassRAMCheck /t reg_dword /d 0x00000001 /f"
        

    def add_offlineservicing_pass(self, enable_user_acc_control: None | bool = None,
                                  enable_code_integrity: None | bool = None):
        offlinescpass = ET.SubElement(self.root, "settings", {"pass": "offlineServicing"})

        # Component description
        component_winsetup = ET.SubElement(offlinescpass, "component",
                                           {"name": "Microsoft-Windows-Setup",
                                            "processorArchitecture": f"{self.architecture}",
                                            "publicKeyToken": "31bf3856ad364e35",
                                            "language": "neutral",
                                            "versionScope": "nonSxS"

                                            })
        # User Account Control
        # EnableLUA specifies whether Windows User Account Controls (UAC) notifies the user when programs try to make changes to the computer.
        # UAC was formerly known as Limited User Account (LUA).
        if enable_user_acc_control is not None:
            component_luasettings = ET.SubElement(offlinescpass, "component",
                                                  self.component("Microsoft-Windows-LUA-Settings"))
            if enable_user_acc_control:
                ET.SubElement(component_luasettings, "EnableLUA").text = "true"
            else:
                ET.SubElement(component_luasettings, "EnableLUA").text = "false"
        #     The Microsoft-Windows-CodeIntegrity component is new in Windows 10, version 1803.
        #     Use the SKUPolicyRequired setting to indicate whether a Windows 10 device will run in S mode on next boot.
        if enable_code_integrity is not None:
            component_codeintegrity = ET.SubElement(offlinescpass, "component",
                                                    {"name": "Microsoft-Windows-CodeIntegrity",
                                                     "processorArchitecture": f"{self.architecture}",
                                                     "publicKeyToken": "31bf3856ad364e35",
                                                     "language": "neutral",
                                                     "versionScope": "nonSxS"

                                                     })
            if enable_code_integrity:
                ET.SubElement(component_codeintegrity, "SkuPolicyRequired").text = "1"
            else:
                ET.SubElement(component_codeintegrity, "SkuPolicyRequired").text = "0"

    def add_oobe_pass(self, users: list[User], inputlocale: None | list = None, systemlocale: str = "en-US",
                      userlocale: str = "hu-HU", setuplang: str = "en-US",firstlogoncommands:list=[]):
        if inputlocale is None:
            inputlocale = ["en-US"]
        oobepass = ET.SubElement(self.root, "settings", {"pass": "oobeSystem"})
        # Hide EULA page.Automatically accepted
        component_wincore = ET.SubElement(oobepass, "component", self.component("Microsoft-Windows-International-Core"))

        if len(inputlocale) == 1:
            # https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-international-core-inputlocale
            ET.SubElement(component_wincore, "InputLocale").text = inputlocale[0]
        else:
            #         If multiple keyboard languages are needed, add them separated with commas
            tmp = "; ".join(inputlocale)
            ET.SubElement(component_wincore, "InputLocale").text = tmp
        ET.SubElement(component_wincore, "SystemLocale").text = systemlocale
        ET.SubElement(component_wincore, "UILanguage").text = setuplang
        ET.SubElement(component_wincore, "UserLocale").text = userlocale

        #         user settings
        component_shellsetup = ET.SubElement(oobepass, "component", self.component("Microsoft-Windows-Shell-Setup"))
        useraccounts = ET.SubElement(component_shellsetup, "UserAccounts")
        localaccounts = ET.SubElement(useraccounts, "LocalAccounts")
        for x in users:
            localaccount = ET.SubElement(localaccounts, "LocalAccount", {"wcm:action": "add"})
            ET.SubElement(localaccount, "Name").text = x.username
            ET.SubElement(localaccount, "Group").text = x.role
            passelement = ET.SubElement(localaccount, "Password")
            ET.SubElement(passelement, "Value").text = x.password
            ET.SubElement(passelement, "PlainText").text = "true"
            #Wallpaper
            themeparent=ET.SubElement(localaccount,"Themes")
            themename=ET.SubElement(themeparent,"ThemeName")
            ET.SubElement(themeparent,"DesktopBackground").text="%WINDIR%\web\wallpaper\\valami.png"

        oobe = ET.SubElement(component_shellsetup, "OOBE")
        ET.SubElement(oobe, "HideEULAPage").text = "true"
        ET.SubElement(oobe, "HideOEMRegistrationScreen").text = "true"
        ET.SubElement(oobe, "HideWirelessSetupInOOBE").text = "true"
        ET.SubElement(oobe, "ProtectYourPC").text = "1"
        #First Logon Commands
        for priority,x in enumerate(firstlogoncommands):
            synccommand=ET.SubElement(oobepass,"SynchronousCommand", {"wcm:action": "add"})
            ET.SubElement(synccommand,"Order").text = str(priority+1)
            ET.SubElement(synccommand,"Description").text= f"Command Number {priority}"
            ET.SubElement(synccommand,"RequiresUserInput").text="false"
            ET.SubElement(synccommand,"CommandLine").text=x



#TODO: Disk things
#TODO: Winget package installs
#TODO: Support for custom files(eg.Wallpapers)


x = Writer()
x.add_win_pe_pass(virtual_machine=True,setuplang="hu-HU",inputlocale=["hu-HU"],windowsedition="Professional",systemlocale="hu-HU")
x.add_offlineservicing_pass(enable_user_acc_control=True, enable_code_integrity=False)
alexusere = User("Administrators", "Csalexke", "alex")
alexmasikusere = User("Users","CsUser","user")
alexlistaja = [alexusere,alexmasikusere]
x.add_oobe_pass(alexlistaja,firstlogoncommands=['Powershell -command Invoke-WebRequest -Uri "https://chocolatey.org/install.ps1" -OutFile $env:temp\install.ps1','powershell -executionpolicy unrestricted -command Unblock-File $env:temp\install.ps1; powershell -command $env:temp\install.ps1'])
x.write()
