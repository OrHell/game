import os,glob
import webbrowser
import shutil
import progressbar
newpath = r'C:\\hack\\boy'
if not os.path.exists(newpath):
	os.makedirs(newpath)
folder = 'C:\\'
for folder, subfolders, files in os.walk(folder):
	for file in files:
		if file.endswith(".exe"):
			print(file)
input()



