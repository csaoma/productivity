import time as t
from datetime import datetime
blocked_urls = ['facebook.com', 'youtube.com', 'netflix.com', 'instagram.com', 'reddit.com', 'twitter.com']
##these are websites that wil be blocked


#this function will add www to the blocked url list
def add_www():
	extra_urls = []
	for url in blocked_urls:
		new_url = f'www.{url}'
		extra_urls.append(new_url)

	blocked_urls.extend(extra_urls)

add_www()


hostsfile = "hosts"
#the file location in windows is C:\WINDOWS\system32\drivers\etc\hosts

redirect_to = "127.0.0.1"


current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
start_time = 7
end_time = 20

while True:
	if datetime(current_year,current_month,current_day,end_time) > datetime.now() > datetime(current_year,current_month,current_day,start_time):
		##if the current time is between the start time and end time then add websites to the redirect list
		
		try: 
			print("running website blocker")
			with open(hostsfile, "r+") as f:
			
				text = f.read()
				for url in blocked_urls:
			 		if url not in text:
			 			f.write(f'{redirect_to} {url}')
			 			f.write('\n')
			 		else:
			 			pass
		except FileNotFoundError:
			text = None
		# using try and except will prevent any unwanted results
			 	
	else:
		with open(hostsfile,"r+") as f:
		    text = f.readlines()
		    f.seek(0)
		    for line in text:
		        
		        if not any(url in line for url in blocked_urls):
		        	f.write(line)
		        f.truncate()

	t.sleep(3)
	#will pause the program every x amount of seconds
