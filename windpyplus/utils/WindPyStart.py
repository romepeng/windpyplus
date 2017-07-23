import subprocess
import os
from WindPy import w

def _startWindExe():
    print("Start WindNET.exe.")
    subprocess.Popen(['C:\\Wind\\Wind.NET.Client\\WindNET\\bin\\WindNET.exe'])
    pass

def _windPyStart():
    w.start()
    print("w.isconnected: {}".format(w.isconnected()))
    
def wConnect():
    if w.isconnected():
        print("w.isconnected: {}".format(w.isconnected()))
        #continue
    elif os.system('tasklist | find "wmain.exe"') == 0 :
        _windPyStart()
    else:
        _startWindExe()
        _windPyStart()

if __name__ == '__main__':
    wConnect()





