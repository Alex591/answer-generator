
from gettext import install
import subprocess
def installer(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def run_batch_file(file_path):
    Popen(file_path,creationflags=subprocess.CREATE_NEW_CONSOLE)


# Example
if __name__ == '__main__':
    import sys
    import os
    from subprocess import Popen


   # telepités
    installer("qt-material")

    

