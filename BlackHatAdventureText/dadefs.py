import __main__
from time import sleep

from DigitalAdventure import dastrings
from src.adminpanel import admin_panel
from src.choices import make_a_choice as mac
from src.cls import cls
from src.database import config
from src.playagain import play_again
from src.player import Player
from src.printer import printer as prn
from src.tupu import tupu


########## INTRO DEFS #############

def init():
	
	global you 
	you = Player(__main__.handle,[])
	intro_turn_on_computer()

def intro_turn_on_computer(choices=1):
	
	prn(dastrings.intro_turn_on_computer_text)
	tmp = mac(1)
	if tmp == '1':
		intro_open_terminal()
		

		
	
def intro_open_terminal(choices=2):
	
	prn(dastrings.intro_open_terminal_text)
	tmp = mac(choices)
	if tmp == '1':
		recon_whois()
	elif tmp == '2':
		recon_protonvpn()
	
		
	
	
	
########## RECON DEFS #############		
	
def recon_whois(choices=3):
	
	prn(dastrings.recon_whois_text)
	tmp = mac(choices)
	if tmp == '1':
		prn(dastrings.aggressive_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	elif tmp == '2':
		prn(dastrings.aggressive_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	elif tmp == '3':
		scanning_nmap_fin()
		
	
	
def recon_protonvpn(choices=3):
	
	prn(dastrings.recon_protonvpn_text)
	config.easterVPN = True
	tmp = mac(choices)
	if tmp == '1':
		prn(dastrings.aggressive_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	elif tmp == '2':
		prn(dastrings.aggressive_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	elif tmp == '3':
		scanning_nmap_fin()
	
	
########## SCANNING DEFS #############	
	
def scanning_nmap_fin(choices=4):
	
	prn(dastrings.scanning_nmap_fin_text)
	tmp = mac(choices)
	if tmp == '1':
		prn(dastrings.default_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()		
	elif tmp == '2':
		prn(dastrings.default_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	elif tmp == '3':
		if config.easterDIR == True:
			exploiting_firefox_with_dir()
		elif config.easterDIR == False:
			exploiting_firefox_restricted()
	elif tmp == '4':
		scanning_dirsearch()
	
	
def scanning_dirsearch(choices=1):
	
	prn(dastrings.scanning_dirsearch_text)
	config.easterDIR = True
	tmp = mac(choices)
	if tmp == '1':
		scanning_nmap_fin()
	
	
	
########## EXPLOITING DEFS #############	
	
def exploiting_firefox_restricted(choices=3):
	
	prn(dastrings.exploiting_firefox_restricted_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_sqli()
	elif tmp == '2':
		exploiting_firefox_admin_panel()
	elif tmp == '3':
		scanning_nmap_fin()
	
def exploiting_firefox_with_dir(choices=4):
	
	prn(dastrings.exploiting_firefox_with_dir_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_sqli()
	elif tmp == '2':
		exploiting_firefox_admin_panel()
	elif tmp == '3':
		exploiting_firefox_slash_assets()
	elif tmp == '4':
		scanning_nmap_fin()
	
	
def exploiting_firefox_sqli(choices=2):
	
	prn(dastrings.exploiting_firefox_sqli_text)
	tmp = mac(choices)
	if tmp == '1' and config.easterDIR is True:
		exploiting_firefox_with_dir()
	elif tmp == '1' and config.easterDIR is not True:
		exploiting_firefox_restricted()
	elif tmp == '2':
		prn(dastrings.aggressive_failure_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()


def exploiting_firefox_admin_panel(choices=2):

	prn(dastrings.exploiting_firefox_admin_panel_text)
	tmp = mac(choices)
	if tmp == '1' and config.easterDIR is True:
		exploiting_firefox_with_dir()
	elif tmp == '1' and config.easterDIR is not True:
		exploiting_firefox_restricted()
	elif tmp == '2':
		exploiting_firefox_admin_panel_attempt()
		
		
	
def exploiting_firefox_admin_panel_attempt():
	
	attempt = 'foo'
	valid = (config.easterU,config.easterP)
	
	while attempt != valid:
		attempt = admin_panel()
		user = tupu(attempt,1)


		if attempt == valid:
			exploiting_firefox_access_granted()
	
	
		#NOT WORKING
		elif str(user) in config.easterList:
			prn(dastrings.exploiting_firefox_admin_panel_high_profile_text + dastrings.anytime_failure_text)
			
			if play_again():
				intro_turn_on_computer()
			else:
				exit()
		
		else:
			print('''
			 
	This user/password combination is not valid..
	
			''')
			config.easterLogCount += 1
			if config.easterLogCount > 2:
				prn(dastrings.exploiting_firefox_admin_panel_high_profile_text + dastrings.anytime_failure_text)
				
				if play_again():
					intro_turn_on_computer()
				else:
					exit()
		
		
	
	
def exploiting_firefox_slash_assets(choices=8):
	
	prn(dastrings.exploiting_firefox_slash_assets_text)
	tmp = mac(choices)
	if tmp == '7' and config.easterVPN:
		prn(exploiting_firefox_slash_assets_good_with_vpn())
	elif tmp == '7' and not config.easterVPN:
		prn('''
		
	Your station disconnects.
		
		''' + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	else:
		exploiting_firefox_slash_assets_bad()
	
		
def exploiting_firefox_slash_assets_bad(choices=1):
	
	prn(dastrings.exploiting_firefox_slash_assets_bad_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_slash_assets()
	
	
	
def exploiting_firefox_slash_assets_good_with_vpn(choices=4):
	
	prn(dastrings.exploiting_firefox_slash_assets_good_with_vpn_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_assets_file()
	elif tmp == '2':
		exploiting_firefox_assets_cat()
	elif tmp == '3':
		exploiting_firefox_assets_ls()
	elif tmp == '4':
		exploiting_firefox_assets_read()
	
	
	
def exploiting_firefox_assets_file(choices=1):
	
	prn(dastrings.exploiting_firefox_assets_file_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_slash_assets()
	
	
def exploiting_firefox_assets_cat(choices=2):
	
	sleep(2)
	print(dastrings.exploiting_firefox_assets_cat_code_text)
	sleep(2)
	print(dastrings.exploiting_firefox_assets_cat_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_slash_assets()
	elif tmp == '2':
		#can be assumed that easterDIR is true since they're here
		exploiting_firefox_with_dir()
	
	
def exploiting_firefox_assets_ls(choices=1):
	
	prn(dastrings.exploiting_firefox_assets_ls_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_slash_assets()	
	
	
def exploiting_firefox_assets_read(choices=1):
	
	prn(dastrings.exploiting_firefox_assets_read_text)
	tmp = mac(choices)
	if tmp == '1':
		exploiting_firefox_slash_assets()	
	
	
def exploiting_firefox_access_granted(choices=2):
	
	prn(dastrings.exploiting_firefox_access_granted_text)
	tmp = mac(choices)
	if tmp == '1':
		prn(dastrings.exploiting_firefox_access_granted_wget_text + dastrings.anytime_failure_text)
		if play_again():
			intro_turn_on_computer()
		else:
			exit()
	
	elif tmp == '2':
		footholded()
		


########## FOOTHOLDED DEFS #############

def footholded(choices=3):
	
	prn(dastrings.footholded_text)
	tmp = mac(choices)
	if tmp == '1':
		footholded_find()
	elif tmp == '2':
		footholded_curl()
		
	elif tmp == '3':
		footholded_uname()
	
	

def footholded_find(choices=1):
	
	prn(dastrings.footholded_find_text)
	tmp = mac(choices)
	if tmp == '1':
		footholded()
	

def footholded_curl(choices=0):
	
	prn(dastrings.footholded_curl_text)
	if play_again():
		intro_turn_on_computer()
	else:
		exit()
	

def footholded_uname(choices=1):
	
	prn(dastrings.footholded_uname_text)
	tmp = mac(choices)
	if tmp == '1':
		rooted_success()
	
	
########## ROOTED DEFS #############

def rooted_success(choices=0):

	print(dastrings.rooted_success_text)
	cls()
	sleep(1)
	print(dastrings.rooted_success_text)
	cls()
	sleep(1)
	print(dastrings.rooted_success_text)
	cls()
	sleep(1)
	print(dastrings.rooted_success_text)
	cls()
	sleep(1)
	print(dastrings.rooted_success_text)	
	
	sleep(3)
	print('''
	root@SpaceZ:~$ passwd''')
	sleep(3)
	print('''
	root@SpaceZ:~$        ''')
	sleep(3)
	print(''' 
	root@SpaceZ:~$ cd ~/Documents/Manifests/Upcoming/''')
	sleep(3)
	print('''
	root@SpaceZ:~$ cp ConfirmedNames.txt DeniedNames.txt''')
	sleep(3)
	print('''
	root@SpaceZ:~$ sudo echo {PLAYER_NAME} > ConfirmedNames.txt'''.format(PLAYER_NAME=you.handle))
	sleep(3)
	print('''
	root@SpaceZ:~$ sudo chmod 440 ConfirmedNames.txt && logout''')
	sleep(3)
	print('''
	
	
	YOUR VENGEANCE IS ETERNAL!
	
	---------------------
	
	Thank you for playing! Great work making it through!
	
	''')
	sleep(3)
	exit()
	






























	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
if __name__ == '__main__':

	intro_turn_on_computer(1)
