

username="CsAlex"
userpass="alex"
pcname="Alex-pc"
description="tesztpc"
language="hu-HU"
organization= "Organ"
wallpapers=[]
fle=open("autounattend.xml","w")








print(f'',file=fle)
print(f'',file=fle)
print(f'<?xml version="1.0" encoding="utf-8"?>',file=fle)
print(f'<unattend xmlns="urn:schemas-microsoft-com:unattend">',file=fle)
print(f'<settings pass="windowsPE">',file=fle)
print(f'<component name="Microsoft-Windows-International-Core-WinPE" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<SetupUILanguage>',file=fle)
print(f'<UILanguage>{language}</UILanguage>',file=fle)
print(f'</SetupUILanguage>',file=fle)
print(f'<InputLocale>040e:0000040e</InputLocale>',file=fle)
print(f'<SystemLocale>{language}</SystemLocale>',file=fle)
print(f'<UILanguage>{language}</UILanguage>',file=fle)
print(f'<UILanguageFallback>{language}</UILanguageFallback>',file=fle)
print(f'<UserLocale>{language}</UserLocale>',file=fle)
print(f'</component>',file=fle)
print(f'<component name="Microsoft-Windows-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'',file=fle)
print(f'<UserData>',file=fle)
print(f'<ProductKey>',file=fle)
print(f'<!-- Do not uncomment the Key element if you are using trial ISOs -->',file=fle)
print(f'<!-- You must uncomment the Key element (and optionally insert your own key) if you are using retail or volume license ISOs -->',file=fle)
print(f'<Key></Key>',file=fle)
print(f'<WillShowUI>Never</WillShowUI>',file=fle)
print(f'</ProductKey>',file=fle)
print(f'<AcceptEula>true</AcceptEula>',file=fle)
print(f'<FullName>{username}</FullName>',file=fle)
print(f'<Organization>{organization}</Organization>',file=fle)
print(f'</UserData>',file=fle)
print(f'</component>',file=fle)
print(f'</settings>',file=fle)
print(f'<settings pass="offlineServicing">',file=fle)
print(f'<component name="Microsoft-Windows-LUA-Settings" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<EnableLUA>true</EnableLUA>',file=fle)
print(f'</component>',file=fle)
print(f'</settings>',file=fle)
print(f'<settings pass="generalize">',file=fle)
print(f'<component name="Microsoft-Windows-Security-SPP" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<SkipRearm>1</SkipRearm>',file=fle)
print(f'</component>',file=fle)
print(f'</settings>',file=fle)
print(f'<settings pass="specialize">',file=fle)
print(f'<component name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<InputLocale>040e:0000040e</InputLocale>',file=fle)
print(f'<SystemLocale>{language}</SystemLocale>',file=fle)
print(f'<UILanguage>{language}</UILanguage>',file=fle)
print(f'<UILanguageFallback>{language}</UILanguageFallback>',file=fle)
print(f'<UserLocale>{language}</UserLocale>',file=fle)
print(f'</component>',file=fle)
print(f'<component name="Microsoft-Windows-Security-SPP-UX" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<SkipAutoActivation>true</SkipAutoActivation>',file=fle)
print(f'</component>',file=fle)
print(f'<component name="Microsoft-Windows-SQMApi" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<CEIPEnabled>0</CEIPEnabled>',file=fle)
print(f'</component>',file=fle)
print(f'<component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<ComputerName>{pcname}</ComputerName>',file=fle)
print(f'<ProductKey>W269N-WFGWX-YVC9B-4J6C9-T83GX</ProductKey>',file=fle)
print(f'</component>',file=fle)
print(f'</settings>',file=fle)
print(f'<settings pass="oobeSystem">',file=fle)
print(f'<component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',file=fle)
print(f'<AutoLogon>',file=fle)
print(f'<Password>',file=fle)
print(f'<Value>{userpass}</Value>',file=fle)
print(f'<PlainText>true</PlainText>',file=fle)
print(f'</Password>',file=fle)
print(f'<Enabled>false</Enabled>',file=fle)
print(f'<Username>{username}</Username>',file=fle)
print(f'</AutoLogon>',file=fle)
if wallpapers:
    print(f'<Themes>',file=fle)
    print(f'            <ThemeName>Theme</ThemeName>',file=fle)
    for x in wallpapers:
        print(f'            <DesktopBackground>%WINDIR%\web\wallpaper\{x}</DesktopBackground>',file=fle)
    print(f'        </Themes>',file=fle)
print(f'<OOBE>',file=fle)
print(f'<HideEULAPage>true</HideEULAPage>',file=fle)
print(f'<HideOEMRegistrationScreen>true</HideOEMRegistrationScreen>',file=fle)
print(f'<HideOnlineAccountScreens>true</HideOnlineAccountScreens>',file=fle)
print(f'<HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>',file=fle)
print(f'<NetworkLocation>Home</NetworkLocation>',file=fle)
print(f'<SkipUserOOBE>true</SkipUserOOBE>',file=fle)
print(f'<SkipMachineOOBE>true</SkipMachineOOBE>',file=fle)
print(f'<ProtectYourPC>1</ProtectYourPC>',file=fle)
print(f'</OOBE>',file=fle)
print(f'<UserAccounts>',file=fle)
print(f'<LocalAccounts>',file=fle)
print(f'<LocalAccount wcm:action="add">',file=fle)
print(f'<Password>',file=fle)
print(f'<Value>{userpass}</Value>',file=fle)
print(f'<PlainText>true</PlainText>',file=fle)
print(f'</Password>',file=fle)
print(f'<Description>{description}</Description>',file=fle)
print(f'<DisplayName>{username}</DisplayName>',file=fle)
print(f'<Group>Administrators</Group>',file=fle)
print(f'<Name>{username}</Name>',file=fle)
print(f'</LocalAccount>',file=fle)
print(f'</LocalAccounts>',file=fle)
print(f'</UserAccounts>',file=fle)
print(f'<RegisteredOrganization>{organization}</RegisteredOrganization>',file=fle)
print(f'<RegisteredOwner>{username}</RegisteredOwner>',file=fle)
print(f'<DisableAutoDaylightTimeSet>true</DisableAutoDaylightTimeSet>',file=fle)
print(f'<FirstLogonCommands>',file=fle)
print(f'<SynchronousCommand wcm:action="add">',file=fle)
print(f'<Description>Control Panel View</Description>',file=fle)
print(f'<Order>1</Order>',file=fle)
print(f'<CommandLine>reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel" /v StartupPage /t REG_DWORD /d 0 /f</CommandLine>',file=fle)
print(f'<RequiresUserInput>true</RequiresUserInput>',file=fle)
print(f'</SynchronousCommand>',file=fle)
print(f'<SynchronousCommand wcm:action="add">',file=fle)
print(f'<Order>2</Order>',file=fle)
print(f'<Description>Control Panel Icon Size</Description>',file=fle)
print(f'<RequiresUserInput>false</RequiresUserInput>',file=fle)
print(f'<CommandLine>reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel" /v AllItemsIconView /t REG_DWORD /d 0 /f</CommandLine>',file=fle)
print(f'</SynchronousCommand>',file=fle)
print(f'<SynchronousCommand wcm:action="add">',file=fle)
print(f'<Order>3</Order>',file=fle)
print(f'<RequiresUserInput>false</RequiresUserInput>',file=fle)
print(f'<CommandLine>cmd /C wmic useraccount where name="{username}" set PasswordExpires=false</CommandLine>',file=fle)
print(f'<Description>Password Never Expires</Description>',file=fle)
print(f'</SynchronousCommand>',file=fle)
print(f'</FirstLogonCommands>',file=fle)
print(f'<TimeZone>GTB Standard Time</TimeZone>',file=fle)
print(f'</component>',file=fle)
print(f'</settings>',file=fle)
print(f'</unattend>',file=fle)
