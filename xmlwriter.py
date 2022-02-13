from xml.dom import minidom
from xml.etree import ElementTree as ET
import handler

class Writer():
    def __init__(self):
        self.root=ET.Element("unattend",{"xmlns":"urn:schemas-microsoft-com:unattend",
                                         "xmlns:wcm": "http://schemas.microsoft.com/WMIConfig/2002/State"})
        # self.document=minidom.Document()
        # self.root = self.document.createElement("unattend")
        # self.root.setAttribute("xmlns", "urn:schemas-microsoft-com:unattend")
        # self.document.appendChild(self.root)

    def add_win_pe_pass(self, architecture:str="amd64", setuplang:str="en-US", inputlocale:list=None, systemlocale:str="hu-HU", userlocale:str="hu-HU",
                        windowsedition:str="Professional",fullname:str="teszt_elek",organization:str=""):
        if inputlocale is None:
            inputlocale = ["en-US"]
        pepass=ET.SubElement(self.root,"settings",{"pass":"windowsPE"})
        # adds winPE_Core
        component_winpe=ET.SubElement(pepass, "component",
                      {"name": "Microsoft-Windows-International-Core-WinPE",
                       "processorArchitecture": f"{architecture}",
                       "publicKeyToken": "31bf3856ad364e35",
                       "language": "neutral",
                       "versionScope": "nonSxS"

                       })
        setupuilang=ET.SubElement(component_winpe,"SetupUILanguage")
        ET.SubElement(setupuilang,"UILanguage").text=setuplang
        if len(inputlocale)==1:
            # https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-international-core-inputlocale
            ET.SubElement(component_winpe,"InputLocale").text= inputlocale[0]
        else:
            #         If multiple keyboard languages are needed, add them separated with commas
            tmp = "; ".join(inputlocale)
            ET.SubElement(component_winpe,"InputLocale").text = tmp
        ET.SubElement(component_winpe,"SystemLocale").text=systemlocale
        ET.SubElement(component_winpe,"UILanguage").text=setuplang
        ET.SubElement(component_winpe,"UserLocale").text=userlocale
        # adds WinPE_Windows_Setup
        component_winsetup = ET.SubElement(pepass, "component",
                                        {"name": "Microsoft-Windows-Setup",
                                         "processorArchitecture": f"{architecture}",
                                         "publicKeyToken": "31bf3856ad364e35",
                                         "language": "neutral",
                                         "versionScope": "nonSxS"

                                         })
        userdata=ET.SubElement(component_winsetup,"UserData")
        productkey=ET.SubElement(userdata,"ProductKey")
        ET.SubElement(productkey,"Key").text=handler.getproductkey(windowsedition)
        ET.SubElement(productkey,"WillShowUI").text="Never"
        ET.SubElement(userdata,"AcceptEula").text="true"
        ET.SubElement(userdata,"FullName").text=fullname
        ET.SubElement(userdata,"Organization").text=organization

    def add_offlineservicing_pass(self,enable_user_acc_control=True):
        offlinescpass=ET.SubElement(self.root,"settings",{"pass":"offlineServicing"})

    #     User account control
        component_winsetup = ET.SubElement(offlinescpass, "component",
                                           {"name": "Microsoft-Windows-Setup",
                                            "processorArchitecture": "amd64",
                                            "publicKeyToken": "31bf3856ad364e35",
                                            "language": "neutral",
                                            "versionScope": "nonSxS"

                                            })
        if enable_user_acc_control:
            ET.SubElement(component_winsetup,"EnableLUA").text="true"
        else:
            ET.SubElement(component_winsetup, "EnableLUA").text = "false"









    def write(self,filename="autounattendtest.xml"):
        out=ET.tostring(self.root)
        dom=minidom.parseString(out)

        xml_str = dom.toprettyxml(encoding="utf-8", indent="\t")

        with open(filename, "wb") as f:
            f.write(xml_str)


x=Writer()
x.add_win_pe_pass()
x.write()