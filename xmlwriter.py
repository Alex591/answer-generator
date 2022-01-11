from xml.dom import minidom
from xml.etree import ElementTree as ET


class Writer():
    def __init__(self):
        self.root=ET.Element("unattend",{"xmlns":"urn:schemas-microsoft-com:unattend",
                                         "xmlns:wcm": "http://schemas.microsoft.com/WMIConfig/2002/State"})
        # self.document=minidom.Document()
        # self.root = self.document.createElement("unattend")
        # self.root.setAttribute("xmlns", "urn:schemas-microsoft-com:unattend")
        # self.document.appendChild(self.root)

    def add_win_pe_pass(self,architecture:str="amd64",setuplang:str="en-US",inputlocale:str=None,systemlocale:str=None,UserLocale:str=None):
        pepass=ET.SubElement(self.root,"settings",{"pass":"windowsPE"})
        # component
        component=ET.SubElement(pepass, "component",
                      {"name": "Microsoft-Windows-International-Core-WinPE",
                       "processorArchitecture": f"{architecture}",
                       "publicKeyToken": "31bf3856ad364e35",
                       "language": "neutral",
                       "versionScope": "nonSxS"

                       })
        ET.SubElement(component,"UILanguage").text=setuplang
        ET.SubElement(component,"InputLocale").text="040e:0000040e"

    def write(self,filename="autounattendtest.xml"):
        out=ET.tostring(self.root)
        dom=minidom.parseString(out)

        xml_str = dom.toprettyxml(encoding="utf-8", indent="\t")

        with open(filename, "wb") as f:
            f.write(xml_str)


x=Writer()
x.add_win_pe_pass()
x.write()