#File: perk.py
#Name: John J.
#Description: This program runs in conjunction with a text file containing one intiger per line. It will sort the number in increasing value 
def perksort(numbers):
	length = len(numbers) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if numbers[i] > numbers[i+1]:
				sorted = False
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

def main():
	numbers = []
	temp = []
	textFile = input("Name of textFile to sort:")
	with open(textFile, 'r', encoding = "UTF-8") as infile:
		for line in infile:
			numbers = numbers + [int(line.strip())]
		temp = numbers
		print("Unsorted List: ", temp) 
		perksort(numbers)
		print("Sorted List: ", numbers)
main()