from xml.dom import minidom



class Writer():
    def __init__(self):

        self.document=minidom.Document()
        self.root = self.document.createElement("unattend")
        self.root.setAttribute("xmlns", "urn:schemas-microsoft-com:unattend")
        self.document.appendChild(self.root)

    def add_win_pe_pass(self,architecture:str="amd64",setuplang:str="en-US"):
        pepass=self.document.createElement("settings")
        pepass.setAttribute("pass","windowsPE")
        # componentname is a standard
        componentname=self.document.createElement("component")
        componentname.setAttribute("name","Microsoft-Windows-International-Core-WinPE")
        componentname.setAttribute("processorArchitecture",architecture)
        componentname.setAttribute("publicKeyToken","31bf3856ad364e35")
        componentname.setAttribute("language","neutral")
        componentname.setAttribute("versionScope", "nonSxS")
        componentname.setAttribute("xmlns:wcm", "http://schemas.microsoft.com/WMIConfig/2002/State")
        componentname.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        pepass.appendChild(componentname)
        # setup language
        s_uilang=self.document.createElement("SetupUILanguage")
        uilang=self.document.createElement("UILanguage")
        uilang.setAttribute(setuplang)
        s_uilang.appendChild(uilang)
        pepass.appendChild(uilang)




        self.root.appendChild(pepass)

    def write(self,filename="autounattendtest.xml"):
        xml_str = self.document.toprettyxml(encoding="utf-8", indent="\t")



        with open(filename, "wb") as f:
            f.write(xml_str)

x=Writer()
x.add_win_pe_pass()
x.write()