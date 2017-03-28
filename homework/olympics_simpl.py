#File: olympics_simple.py
#Name: John J.
#Description: This program works in addition to the athletes.txt file to find the both the amount of gold medalists in a year in question and the medals won by a perticular athlete in the year in question
def date():
	"""
	The date function asks for the year that the user is asking for.
	This function then takes each line of the file for the value of that line stripped. It then uses the readline()
	function to check the nextline to see if it is equal to 1. This is because gold medal is equal to one.
	If that line is equal to 1 it will add 1 to the variable and then returns the value for the medal.
	"""
	medal = 0
	with open('athletes.txt', 'r', encoding = "UTF-8") as infile:
		for line in infile:
			if line.strip() == year:
				if infile.readline().strip() == '1'.strip():
					medal += 1
	return medal

def name(last, first):
	"""
	The name function looks through the textg file when the user inputs the name of the athelete they are searching
	for. All the medal types (gold, silver, and bronze) start with a value of zero. It will then strip the name of
	the medal and will add 1 to either gold, silver, or bronze depending on how many medals the athelete won for 
	that type of medal. It will then display that value for that type of medal.
	"""
	
	gold = 0
	silver = 0
	bronze = 0

	with open('athletes.txt', 'r', encoding = "UTF-8") as infile:
		for line in infile:
			if line.strip() == last.upper().strip():
				if infile.readline().strip() == first.upper().strip():
					infile.readline()
					medal = infile.readline()
					if medal.strip() == '1'.strip():
						gold += 1
					elif medal.strip() == '2'.strip():
						silver += 1
					elif medal.strip() == '3'.strip():
						bronze += 1
	return gold, silver, bronze

def main():

	year = input('Enter a year to count its winners: ')
	medal = date(year)
	print('In the year ' + year + ' there were ' + str(medal) + ' gold medalists in total.')
	print("Let's look up the total medals won by an athlete (1896-2008)!")
	last = input('Last name: ')
	first = input('First name: ')
	g, s, b = name(last, first)
	print(first + " " + last + " won " + str(g) + " gold, " + str(s) + " silver and " + str(b) + " bronze medals.")

main()