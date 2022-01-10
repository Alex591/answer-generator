def getProductkey(edition: str)->str:
    # Docs: https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj612867(v=ws.11)?redirectedfrom=MSDN
    # https://www.tenforums.com/tutorials/96683-create-media-automated-unattended-install-windows-10-a.html
    assert edition in ["Professional","Professional N","Enterprise","Enterprise N","Education",
                       "Education N","Home","Pro"]
    