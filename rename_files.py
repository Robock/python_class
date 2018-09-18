import os
def secret_message():
	file_names = os.listdir(r"C:\Users\Hank2\Desktop\secret")
	saved_path = os.getcwd()
	os.chdir(r"C:\Users\Hank2\Desktop\secret")
	for pic_files in file_names:
		os.rename(pic_files, pic_files.translate(None,"0123456789"))
	os.chdir(saved_path)

secret_message()