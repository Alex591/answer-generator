from xml.etree import ElementTree as ET


# helper file that provides classes

class Partiton():
    """
    Defines a basic partition.

    ...

    Attributes

    format: str
        test
    label: str
        test2
    size: int
        The drive size in Megabytes
    letter:
        A letter label for the partition. Must be an ASCII character.


    """
    def __init__(self, format: str = None, label: str = None, size: int = None, letter: str = None, extend: bool = None,
                 type: str = "", typeid: str = None, order: int = None) -> None:
        self.label = label
        self.order = order
        self.format = format
        self.size = size
        self.letter = letter
        self.type = type
        self.extend = extend
        self.typeid = typeid

    def createpartition(self):

        result = {}
        result["Order"] = str(self.order)
        result["Type"] = self.type
        if not self.extend:
            result["Size"] = str(self.size)
        else:
            result["Extend"] = "true"

        return result

    def modifypartition(self):
        # return a ModifyPartition dict with all necessary components
        result = {}
        result["Order"] = str(self.order)
        result["PartitionID"] = str(self.order)
        if self.label:
            result["Label"] = self.label
        if self.letter:
            result["Letter"] = self.letter
        if self.format:
            result["Format"] = self.format
        if self.typeid:
            result["TypeID"] = self.typeid
        return result
    @property
    def order(self):
        return self.order
    @order.setter
    def order(self, value):
        self.order = value


class HardDrive(Partiton):
    # a singular hard drive that hhas partitions in it
    def __init__(self, wipedisk: bool = True, windowspartition: bool = False) -> None:
        super(Partiton)
        self.wipedisk = wipedisk
        self.__partitionlist = []
        self.__windowspartition = windowspartition

    def setwinpartition(self, label="OS"):
        # Windows RE Tools partition
        winrepartition = Partiton(label="WINRE", format="NTFS", size=300, typeid="DE94BBA4-06D1-4D40-A16A-BFD50179D6AC",
                                  type="Primary")
        # System partition (ESP)
        systempartition = Partiton(type="EFI", size=100, label="System", format="FAT32")
        # Microsoft reserved partition (MSR)
        msrpartition = Partiton(type="MSR", size=128)
        windows_partition = Partiton(type="Primary", label=label, letter="C", format="NTFS", extend=True)
        self.addpartitionlist(winrepartition)
        self.addpartitionlist(systempartition)
        self.addpartitionlist(msrpartition)
        self.addpartitionlist(windows_partition)
        self.partitionorder()

    def partitionorder(self):
        for index, x in enumerate(self.__partitionlist):
            x.order = index + 1

    @property
    def partitionlist(self) -> list[Partiton]:
        return self.__partitionlist

    def addpartitionlist(self, p):
        self.__partitionlist.append(p)

    @property
    def windowspartition(self) -> bool:
        return self.__windowspartition


class User():
    def __init__(self, role: str, username: str, password: str, fullname: str, autologon: bool = False):
        self.__role = role
        self.__username = username
        self.__fullname = fullname
        self.__password = password
        self.autologon = autologon

    def convertpassword(self, password):
        pass

    @property
    def fullname(self) -> str:
        return self.__fullname

    @property
    def role(self) -> str:
        return self.__role

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password


class Registry:
    pass
