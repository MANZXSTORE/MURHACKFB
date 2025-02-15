import requests,json,os,sys,random,datetime,time,re
from time import sleep as turu
from rich import print as cetak
from rich.panel import Panel as nel
from rich.columns import Columns as col
from rich.columns import Columns
from rich.panel import Panel as panel
from rich.console import Console
console = Console()
tokene = []
ses = requests.Session()
gr = '\033[1;32;41m'
#k = '\033[33m'
w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
#b = '\033[1;34m'
#p = '\033[1;35m'
c = '\033[1;36m'
y = '\033[1;33m'
#reset = '\033[0m'
m = '\x1b[1;91m'#MERAH
#
P = '\x1b[1;97m'# 
M = '\x1b[1;91m'#
H = '\x1b[1;92m'#
K = '\x1b[1;93m'#
B = '\x1b[1;94m'#
U = '\x1b[1;95m'#
dx = '\33[m' # DEFAULT
O = '\x1b[1;96m'#
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
#WARNA
m = '\x1b[1;91m' #RED +
#WARNA
k = '\033[93m' # KUNING +
#WARNA
h = '\x1b[1;92m' # HIJAU +
#WARNA
hh = '\033[32m' # HIJAU -
#WARNA
u = '\033[95m' # UNGU
#WARNA
kk = '\033[33m' # KUNING -
#WARNA
b = '\33[1;96m' # BIRU -
#WARNA
p = '\x1b[0;34m' # BIRU +
warna_warni = random.choice([g, r, b, p, y])
tanda = f'{p}[{w}+{p}]{w}'
def res():
	kon = []
	kon.append(panel(f'[red]•[white]Lihat Hasil CP Anda',width=36,subtitle=f'[blue]╭───',subtitle_align='left',title=f"[[red] 01 [/]]",padding=(0,2),style=f"bold blue"))
	kon.append(panel(f'[red]•[white]Lihat Hasil OK Anda',width=36,title=f"[[red] 02 [/]]",padding=(0,2),style=f"bold blue"))
	console.print(Columns(kon))
	kz = input(f'{B}   ├─> {P}: {P}')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' File Tidak Di Temukan ')
			time.sleep(3)
			exit()
		if len(vin)==0:
			print(f' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'\x1b[1;97m{B}   ├─> {P}\x1b[1;93m'+nom+'\x1b[1;91m•\x1b[1;97m'+isi+' Ada \x1b[1;93m'+str(len(hem))+' \x1b[1;97mAkun \x1b[1;97mCP '+w)
				else:
					lol.update({str(cih):str(isi)})
					print(f'\x1b[1;97m{B}   ├─> {P}\x1b[1;93m'+str(cih)+'\x1b[1;91m•\x1b[1;97m'+isi+'\x1b[1;93m'+str(len(hem))+' \x1b[1;97mCP '+w)
			geeh = input(f'{B}   ├─> {P}Pilih 1/'+nom+' : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{B}   ╰─> {P}Pilih Yang Bener sayang ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f'{B}   ╰─> {P}File Tidak Di Temukan ')
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\x1b[1;97m{B}   ├─> {P}\x1b[1;93m{cpkuni[0]}\x1b[1;97m|\x1b[1;93m{cpkuni[1]}\x1b[1;93m')
				nocp +=1
			input(f'{B}   ╰─> {P}Tekan Enter  ')
			exit()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'{tanda} File Tidak Di Temukan ')
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(f'{tanda} Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'\x1b[1;97m{B}   ├─> {P}\x1b[1;92m'+nom+'\x1b[1;91m•\x1b[1;97m'+isi+' Ada \x1b[1;92m'+str(len(hem))+ ' \033[0mAkun Sucses '+w)
				else:
					lol.update({str(cih):str(isi)})
					print(f'\x1b[1;97m{B}   ├─> {P}\x1b[1;92m'+str(cih)+'\x1b[1;91m•\x1b[1;97m'+isi+'\x1b[1;92m '+str(len(hem))+' \033[0mSucses '+w)
			geeh = input(f'{B}   ├─> {P}Pilih 1/'+nom+' : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{B}   ├─> {P}Pilih Yang Bener sayang ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f'{B}   ├─> {P}File Tidak Di Temukan ')
				time.sleep(2)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{B}   ├─> {P}\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input(f'{B}   ╰─> {P}Tekan Enter ')
			exit()
	elif kz in ['0','00']:
		exit()
	else:
		printf(f'{B}   ╰─> {P}Pilih Yang Bener sayang ')
		exit()

def zahra_animasi2(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
def zahra_animasi3(berjalan):
    for gas in str(berjalan) + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.0010)
def cetak_panel(teks, lebar):
    garis_atas = (f'{g}~{w}') * lebar
    teks_tengah = teks.center(lebar)
    garis_bawah = (f'{g}~{w}') * lebar

    panel = f"{garis_atas}\n{teks_tengah}\n{garis_bawah}"
    print(panel)
