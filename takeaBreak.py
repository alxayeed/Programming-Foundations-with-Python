#Take a Break

import time
import webbrowser

start_time = time.ctime()
print('Time started at ',start_time)
for i in range(3):
    time.sleep(5)
    webbrowser.open('youtube.com')
