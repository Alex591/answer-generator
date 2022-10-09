
import string
import os



def getwindowseditions()->dict:
    szotar = {"Professional": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
            "Professional N": "MH37W-N47XK-V7XM9-C7227-GCQG9",
            "Pro for Workstations": "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J",
            "Pro for Workstations N": "9FNHH-K3HBT-3W4TD-6383H-6XYWF",
            "Pro Education": "6TP4R-GNPTD-KYYHQ-7B7DP-J447Y",
            "Pro Education N": "YVWGF-BXNMC-HTQYQ-CPQ99-66QFC",
            "Education": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
            "Education N": "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
            "Enterprise": "NPPR9-FWDCX-D2C8J-H872K-2YT43",
            "Enterprise N": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4",
            "Enterprise G": "YYVX9-NTFWV-6MDM3-9PT4T-4M68B",
            "Enterprise G N": "44RPN-FTY23-9VTTB-MP9BX-T84FV",
            "Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
            "Home Single Language": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
            }
    return szotar


def getproductkey(edition: str) -> str:
    """
    A generic product key is needed to do unattended installations.
    :param edition: str:Windows edition in string format.
    :return: str:Generic product key for each Windows edition


    Works with valid windows editions


    >>> getproductkey("Professional")
    'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    >>> getproductkey("Enterprise G")
    'YYVX9-NTFWV-6MDM3-9PT4T-4M68B'


    But not with invalid ones

    >>> getproductkey("Entelplise")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid edition of Windows



    """
    # Docs:
    # https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj612867(v=ws.11)?redirectedfrom=MSDN
    # https://www.tenforums.com/tutorials/96683-create-media-automated-unattended-install-windows-10-a.html
    # https://docs.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys

    szotar = getwindowseditions()
    assert edition in szotar.keys(), "Invalid edition of Windows"

    return szotar[edition]

def alllanguages()->list:
    """
    Returns the most commonly used languages for the region.
    It does not include all languages to avoid clutter.

    :return: a list of language names
    """
    



    return ["Hungarian","English (United Kingdom)","English (United States)","English (Canada)","Ukrainian","Romanian"]

def inputlocales(language: str) -> str:
    """

    :param language: A language code, such as hu-HU
    :return:
    """
    szotar = {
        "hu-HU": "040e:0000040e",
        "ro-RO": "0418:00010418",
        "uk-UA": "0422:00020422",
        "en-US": "0409:00000409",
        "pl-PL": "0415:00000415",
        "en-GB": "0809:00000809",
        "en-CA": "1009:00000409",
        "en-IE": "1809:00001809",
        "de-AT": "0c07:00000407"


    }
    return szotar[language]

def powerplan(name: str) -> str:
    powerlevels={
        "balanced":"381b4222-f694-41f0-9685-ff5bb260df2e",
        "high performance": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",
        "power saver": "a1841308-3541-4fab-bc81-f71556f20b4a"
    }
    assert name.lower() in powerlevels.keys()
    return powerlevels[name.lower()]


def getdriveletters()->list:
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    return available_drives


if __name__ == '__main__':
    import doctest
    doctest.testmod()

