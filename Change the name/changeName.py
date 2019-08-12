"""I have made to this script to change the episode name of a famous drama,'Kothao keu nei' by Humayun Ahmed
The names were like 'kothao keu nei-01.mkv' type formate,which was not sorted acording to the episode number
So,this scropt will change the name by putting the episode number in front
e.g.,'01.kothao keu nei'
also,in some episodes,there was a slight mistake 'kothai' instead of 'kothao'
This error also resolved"""

import os,re

ep_list = os.listdir('E:\Movie\Movie\Kothao Keu Nei 1990 Legendary Bangla Natok All Episodes Humayun Ahmed 720P WEBHD RIP')

os.chdir('E:\Movie\Movie\Kothao Keu Nei 1990 Legendary Bangla Natok All Episodes Humayun Ahmed 720P WEBHD RIP')
print(os.getcwd())


for old_name in ep_list:
	#correct if the name is 'kothai'
	if old_name[8] =='i':
		print(old_name)
		i = old_name[8]
		new_name = old_name.replace(i,'o')
		print(old_name)
		os.rename(old_name,new_name)
	
	#change by bringing episode number at front	
	ep = new_name[-6:-4]
	final_name = re.sub('-|0|1|2|3|4|5|6|7|8|9','',new_name)
	final_name = ep+'.'+final_name
	os.rename(new_name_name,final_name)
	# print(old_name)
	# print(new_name)

	
	
