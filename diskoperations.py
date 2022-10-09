import string
import os
import shutil
from pathlib import Path
def getdriveletters()->list:
    """
    Gets all the drive letters currently assigned to a drive in the system.

    :return: List of drive letters
    """
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    return available_drives

def delete_from_dir(directory:str)->None:
    """
    Deletes every file from a directory. In this instance it is used to clear up files between program runs.
    :param directory:
    :return:
    """
    for path in Path(directory).glob("**/*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)



def copy_to_oem_folder(driveletter:str):
    """
    Copies the contents of the directory to_copy to %driveletter%/sources/$OEM$
    :param driveletter: Drive letter to copy to
    :return:
    """
    originaldir = os.path.join(os.getcwd(), "$OEM$")
    destinationdir= os.path.join(driveletter,"sources")

    #First we create the directory
    os.makedirs(destinationdir,exist_ok=True)

    #Then we delete everything in the destination dir.
    delete_from_dir(destinationdir)


    shutil.move(originaldir,destinationdir)

    pass

if __name__=="__main__":
    copy_to_oem_folder("D:")