#Take a Break

import time
import webbrowser


for i in range(3):
	start_time = time.ctime()
	print('Time started at ',start_time)
	time.sleep(500)
	webbrowser.open('https://www.youtube.com/watch?v=kbYbvDK-HlY')
