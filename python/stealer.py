
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree

directory = getcwd()+"/Result/"
try:mkdir(directory)
except FileExistsError:pass

listTarget = ['C:\\Users\\Гусев\\Desktop\\test\\tt']

for target in listTarget:
	under = directory + basename(target)
	try:copytree(target, under)
	except:pass
