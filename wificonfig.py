#Generates Wi-Fi configuration files
from xml.etree import ElementTree as ET

class WifiNetwork():
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password
        self.root=  ET.Element("WLANProfile", {"xmlns": "http://www.microsoft.com/networking/WLAN/profile/v1"})
    def create(self):
        pass

