#File: testMyPriorityQueue.py
#Name: John J.
#Description: This program is a test function for myPriorityQueue.py

from myPriorityQueue import *
import airExpress

def main():
	"""
	Test application which was given in the lab
	"""
	pq = createPriorityQueue()
	print("Is the queue empty?", emptyQueue(pq) == True)
	insert(pq, airExpress.Passenger("Fred", 5))
	print("Is front Fred/5?", \
	front(pq).name == "Fred" and front(pq).priority == 5)
	insert(pq, airExpress.Passenger("Wilma", 7))
	print("Is size 2?", pq.size == 2)
	insert(pq, airExpress.Passenger("Pebbles", 6))
	print("Is front Wilma/7?", \
	front(pq).name == "Wilma" and front(pq).priority == 7)
	print("dumping the queue:")
	while not emptyQueue(pq):
		print(remove(pq))

main()