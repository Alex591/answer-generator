
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
    installer('pyqt6')
    installer('pyqt6-tools')

    installer('pyside6')


    ##create desktop shortcut

    miaz=sys.executable
    # sys.executable
    # A string giving the absolute path of the executable binary for the Python interpreter, on systems where this makes sense.
    # If Python is unable to retrieve the real path to its executable, sys.executable will be an empty string or None
    print(miaz)
    hossz=len(miaz)-10
    miaz=miaz[:hossz]
    miaz=miaz+'Lib\site-packages\qt6_applications\Qt\\bin\\designer.exe'
    print(miaz)
    # script=open("script.bat","w")
    # print("@echo off",file=script)
    # print('set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"',file=script)
    # print('echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%',file=script)
    # print('echo sLinkFile = "%USERPROFILE%\Desktop\QT Designer.lnk" >> %SCRIPT%',file=script)
    # print('echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%',file=script)
    # print(f'echo oLink.TargetPath = "{miaz}" >> %SCRIPT%',file=script)
    # print('echo oLink.Save >> %SCRIPT%',file=script)
    # print('cscript /nologo %SCRIPT%',file=script)
    # print('del %SCRIPT%',file=script)
    # print('DEL "%~f0"',file=script)
    # script.close()
    # scriptdir=os.getcwd()+"\script.bat"
    # run_batch_file('script.bat')

