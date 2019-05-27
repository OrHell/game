import random
from random import randint
def lvl_get(lvl):
	lvl = int(lvl)
	if (lvl>100):
		
		return 10
	if (101>lvl>91):

		return 9
	if (91>lvl>81):
		
		return 8
	if (81>lvl>71):
		
		return 7
	if (71>lvl>61):
		
		return 6
	if (61>lvl>51):
		
		return 5
	if (51>lvl>41):
		
		return 4
	if (41>lvl>31):
		
		return 3
	if (31>lvl>21):
		
		return 2
	if (21>lvl>11):
		
		return 1
	if (11>lvl>1):
		
		return 0
	else:
		lvl = '?'
		return lvl
def random_def(rand_element):
	return random.choice(rand_element)

def random_stats():
	return randint(10, 79)

def generate():
	with open('name.txt','r') as file:
		person_name = file.read()
	with open ('class.txt','r') as file:
		person_class= file.read()
	with open ('race.txt','r') as file:
		person_race = file.read()
	with open ('imune.txt','r') as file:
		person_imune= file.read()
	with open ('imune.txt','r') as file:
		person_hole = file.read()

	
	person_class=person_class.split(' ')
	person_name =person_name.split(' ')
	person_race = person_race.split(' ')
	person_imune =person_imune.split(' ')
	person_hole = person_hole.split(' ')
	hole =random_def(person_hole)
	name = random_def(person_name)
	race = random_def(person_race)
	class_p = random_def(person_class)
	imune = random_def(person_imune)

	powe = random_stats()
	agility = random_stats()
	intel = random_stats()

	if class_p == 'Magician ':
		intel = int(intel*2.5)
		powe = int(powe / 2.3)
		agility=int(agility/2)
		level = lvl_get(intel)
	if class_p == 'Warior' or 'Paladin':
		intel = int(intel/2.2)
		powe =int(powe*2)
		agility =int(agility/2.2)
		level = lvl_get(powe)
	if class_p == 'Hunter':
		intel=int(intel*0.4)
		powe= int((powe*0.3)/1.4)
		agility = int(agility*2)
		level = lvl_get(agility)
	if class_p == 'Homeless':
		intel = int(intel*1.5)
		powe = int(powe*1.6)
		agility = int(powe*2)
		level = 10
	helth =int(100 +powe +(((powe/2)*1.2))/0.4)
	mana = int(100 +intel +(((intel/1.1)*1.1))/0.2)

	print("|HP   |","|MP   |","|LVL   |")
	print("|",helth,"|","|",mana,"|","|",level,"   |")
	print("Имя: "+name)
	print("Расса: "+race)
	print("Класс: "+class_p)
	print("Stats")
	print ("Сила: ",powe)
	print("Ловкость: ",agility)
	print("Интелект: ",intel)

	print("Иммунитет: ",imune)
	print("Слабость: ",hole)
	
	return main()



def main():
	print("1.Generate")
	choose = input(">")
	if choose == '1':
		return generate()
if __name__ == '__main__':
	main()