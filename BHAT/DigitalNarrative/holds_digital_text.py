intro_turn_on_computer_text = '''You sit down at your desk and turn on the computer. After decrupting your solid state your environment pops up.'''

intro_open_terminal_text = '''You begin your assault.'''

intro_proton_vpn_text = '''You boot up your VPN and then get to work, a quick WHOIS floods the terminal. Among the output you note an IP range: 10.11.10.0/16. You export this number into the environment variable "range".''' # set up a trap for later which this setting avoids

intro_whois_text = '''Among the output you note an IP range: 10.11.10.0/16. You export this number into the environment variable "range".'''

scanning_masscan_text = '''Your aggressive packet storm is picked up on by SpaceZ Blue Team. Your station is blacklisted.

A few hours later the window of your living room explodes, and a team of CyberCrime RXMP on horseback come jumping through the opening to trample and arrest you.

Months later you are finally tried, and convicted for Conspiracy to Commit Unauthorized Computer Access and Possession of Unauthorized Data.'''

scanning_nmap_all_text = '''Your aggressive packet storm is picked up on by SpaceZ Blue Team. Your station is blacklisted.

A few hours later the window of your living room explodes, and a team of CyberCrime RXMP on horseback come jumping through the opening to trample and arrest you.

Months later you are finally tried, and convicted for Conspiracy to Commit Unauthorized Computer Access and Possession of Unauthorized Data.'''

scanning_nmap_fin_text = '''Your scan comes back with several IPs, the only one that catches your interest is 10.11.242.232. You assign this to the environment variable "ip".

Its output reads:

	21/open
	22/open
	80/open
	3386/open
	61446/open
	61447/open
	61448/open
	61449/open'''
	
scanning_ftp_text = '''The default credentials attempt is picked up on by SpaceZ Blue Team. Your station is blacklisted.

A few hours later the window of your living room explodes, and a team of CyberCrime RXMP on horseback come jumping through the opening to trample and arrest you.

Months later you are finally tried, and convicted for Conspiracy to Commit Unauthorized Computer Access and Possession of Unauthorized Data.'''

scanning_ssh_text = '''The default credentials attempt is picked up on by SpaceZ Blue Team. Your station is blacklisted.

A few hours later the window of your living room explodes, and a team of CyberCrime RXMP on horseback come jumping through the opening to trample and arrest you.

Months later you are finally tried, and convicted for Conspiracy to Commit Unauthorized Computer Access and Possession of Unauthorized Data.'''

scannning_dirsearch_text = '''You directory bust the root and discover a backup file being hosted at "/resources/json/". Within it is a user's SSH Keypair.'''

scanning_firefox_text = '''As you navigate their web portal you feel like there are no leads here at all. Before giving up you decide to walk it once more with Burp tracing in the background.

While loading "https://www.spacez.com/admin", which triggers a redirect back to home, the server response actually carries hardcoded credentials within it!'''

footholding_try_at_admin = '''Great success! Very excite! You are dropped into an administrative interface that appears to have an API within it. Leveraging Pentest-Monkey's PHP Reverse Shell you gain access through this API.

A quick whoami reports:

	www-data

While a ps -aux reports:

	Owner		PID	    Perm	Path

	www-data	139668	    600 	/var/logs/monitor.php
	root		3096	    640	/usr/libexec/fwupd/fwupd
	root		2055	    674	/usr/sbin/cups-browsed	
	root		1254	    600	/lib/systemd/systemd-logind
	root		4101	    600	[loop13]
	jstephen	10059	    647	/usr/bin/log-backup.py
	root		47999	    666	[watchdogd]
	
''' 

footholding_ps_id_fail = '''Your poor choices have been noticed in the logs by SpaceZ Blue Team.

A few hours later the window of your living room explodes, and a team of CyberCrime RXMP on horseback come jumping through the opening to trample and arrest you.

Months later you are finally tried, and convicted for Conspiracy to Commit Unauthorized Computer Access and Possession of Unauthorized Data.'''

footholding_ps_id_success = '''You leverage this scripts insecure permissions to spin up a reverse shell as jstephen. You have gained an official foothold!'''

footholding_try_at_ssh = '''Your login attempt is unsuccessful, this was likely noted by Blue Team.'''

footholding_try_at_ftp = '''Your login attempt is unsuccessful, this was likely noted by Blue Team.'''

footholding_do_a_SQLi = '''Your plebian use of SQLMap to attack the forms is picked up on by SpaceZ Blue Team. Your station is blacklisted.

A few hours later the window of your living room explodes, and a team of CyberCrime RXMP on horseback come jumping through the opening to trample and arrest you.

Months later you are finally tried, and convicted for Conspiracy to Commit Unauthorized Computer Access and Possession of Unauthorized Data.'''

footholding_ssh_in = '''With the keypairs copied onto your machine you are able to SSH into the server. A quick whoami on the inside reports:

	jstephen

You have gained your initial foothold!
'''























