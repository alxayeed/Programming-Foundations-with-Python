#Renaming File

import os
import re



def rename_me(file_list):
	saved_path = os.getcwd()
	print(saved_path)
	os.chdir(r'F:\Practice\Python\Courses\Programming Foundations with Python Videos\Output')
	
	no = 1
	for file in file_list:
		print('{}.The old name is {}'.format(no,file))
		new_file = re.sub('0|1|2|3|4|5|6|7|8|9','',file) #applying regex to find pattern of digits from 'file'
		os.rename(file,new_file)
		print('The new name is ',new_file)
		no +=1
		
		
file_list = os.listdir(r'F:\Practice\Python\Courses\Programming Foundations with Python Videos\Output')
rename_me(file_list)
print(file_list)
	

#[WinError 2] file doesnot exist
# [WinError 183] file already exists