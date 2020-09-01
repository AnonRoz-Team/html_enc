#!/usr/bin/python2.7
# encoding: utf-8
# -*- coding: utf-8 -*-
# Author D4RK5H4D0W5
G0 = '\033[0;32m'
C0 = '\033[0;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests,os,sys
from bs4 import BeautifulSoup as bs
try:
	r=requests.Session()
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
    __  ____            __
   / / / / /_____ ___  / /  ___  ____  _____
  / /_/ / __/ __ `__ \/ /  / _ \/ __ \/ ___/  %sCoded by D4RKSH4D0WS%s
 / __  / /_/ / / / / / /  /  __/ / / / /__    %sIG @anonroz_team%s
/_/ /_/\__/_/ /_/ /_/_/   \___/_/ /_/\___/    %sFB gg.gg/AnonRoz-Team%s
	'''%(C0,W0,C0,W0,C0,W0,C0)
	sys.argv[1]
	print '%s[%s!%s] Waiting ...'%(W0,R0,W0)
	dark=r.get('https://www.smartgb.com/free_encrypthtml.php').text
	ch=bs(dark,'html.parser').find_all('input',attrs={'name':'ch'})[0]['value']
	shadows=r.post('https://www.smartgb.com/free_encrypthtml.php?do=crypt',data={'h':open(sys.argv[1]).read(),'s':'extended','ch':ch,'Skicka':'Encrypt+HTML'}).text
	dadi=bs(shadows,'html.parser').find_all('textarea')[0].text
	print dadi
	open(sys.argv[1]+'_enc.html','a+').write(dadi)
	print '%s[%s✓%s] Done, saved in %s_enc.html'%(W0,G0,W0,sys.argv[1])
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IOError:
	exit('%s[%s!%s] %s file does not exist'%(W0,R0,W0,sys.argv[1]))
except IndexError:
	exit('%s[%s!%s] Use : python2 %s sc.html'%(W0,R0,W0,sys.argv[0]))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] Exit'%(W0,R0,W0))
