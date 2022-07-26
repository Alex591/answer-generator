from xml.etree import ElementTree as ET
#helper file that provides classes

class Partiton():
    #a partition in a hard drive
    def __init__(self,label:str,format:str,typeid=None) -> None:
        self.__label=label
        self.__format=format
    


class HardDrive(Partiton):
    #a singular hard drive that hhas partitions in it
    def __init__(self,wipedisk:bool=True) -> None:
        super(Partiton)
        self.wipedisk=wipedisk
        self.__partitionlist=[]
    
    @property
    def partitionlist(self):
        return self.__partitionlist
    def addpartitionlist(self,p):
        self.__partitionlist.append(p)



    
    


    


class User():
    def __init__(self, role: str, username: str, password: str):
        self.__role = role
        self.__username = username
        self.__password = password
        

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

