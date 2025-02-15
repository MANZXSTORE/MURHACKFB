import os,sys,random,time
from rich.panel import Panel
from rich import print as cetak
from rich.panel import Panel as panel
gr = '\033[1;32;41m'
k = '\033[33m'
w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'
y = '\033[1;33m'
reset = '\033[0m'
def banzar():
    cetak(panel(f"""\n[bold red]  _________  _______    ___ ___    __ __      _____    _______\n  \______  \ \_____ \  /   |   \  /  v  \    /  _  \   \      \  
   |      _/ /   |   \/    ~    \/  \ /  \  /  /_\  \  /   |   \ [bold blue]
   |   |   \/    |    \    Y    /    Y    \/    |    \/    |    \  
   |___|_  /\_______  /\___|_  /\____|__  /\____|__  /\____|__  /
         \/         \/       \/         \/         \/         \/   \n\n       [underline white][italic white]Version :[underline blue] 4.0[underline white] || Author :[underline green] RoHmaN[underline white] || Status :[underline blue] Premium""",width=73,padding=(0,2),title=f"",style=f"bold blue"))

def banlog():
    cetak(panel(f"""\n[bold red]  _________  _______    ___ ___    __ __      _____    _______\n  \______  \ \_____ \  /   |   \  /  v  \    /  _  \   \      \  
   |      _/ /   |   \/    ~    \/  \ /  \  /  /_\  \  /   |   \ [bold blue]
   |   |   \/    |    \    Y    /    Y    \/    |    \/    |    \  
   |___|_  /\_______  /\___|_  /\____|__  /\____|__  /\____|__  /
         \/         \/       \/         \/         \/         \/   \n\n       [underline white][italic white]Version :[underline blue] 4.0[underline white] || Author :[underline green] RoHmaN[underline white] || Status :[underline blue] Premium""",width=73,subtitle=f'[bold blue]╭───',subtitle_align='left',padding=(0,2),title=f"",style=f"bold blue"))
