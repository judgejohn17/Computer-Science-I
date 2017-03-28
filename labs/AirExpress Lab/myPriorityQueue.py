#File: airExpress.py
#Name: John J.
#Description: This program works in conjunction with the airExpress.py and testMyPriorityQueue.py
from rit_object import * 
from myNode import *

class PriorityQueue(rit_object):
    __slots__ = ('front', 'size')
    _types    = (object, int)

def createPriorityQueue():
	"""
	This function creates an empty Node.
	"""
    return PriorityQueue(None, 0)

def insert(PriorityQueue, element):
	"""
	This function is repsonsible for taking the passengers and putting them into the queue. It puts
	them in decending order at all time.
	"""
    newNode = Node(element, None)
    if(emptyQueue(PriorityQueue)):
            PriorityQueue.front=newNode
    elif(PriorityQueue.front.data.priority < element.priority):
            newNode.next = PriorityQueue.front
            PriorityQueue.front = newNode
    else:
            previous = None
            current = PriorityQueue.front
            is_unchanged = True
            while is_unchanged is True and current is not None:
                    if current.data.priority < newNode.data.priority:
                            is_unchanged = False
                            newNode.next = current
                            previous.next = newNode
                    previous = current
                    current = current.next
            if is_unchanged is True:
                    previous.next = newNode
    PriorityQueue.size += 1

def front(queue):
    """ 
    This program returns the front element of the queue
    """
    if emptyQueue(queue):
        raise IndexError("Front from empty queue")
    else:
        return queue.front.data

def remove(PriorityQueue):
	"""
	This function removes the first element in the queue and returns a reference.
	"""
        if emptyQueue(PriorityQueue):
                raise IndexError("Cannot remove on empty queue")
        temp_data = PriorityQueue.front.data
        PriorityQueue.front = PriorityQueue.front.next
        PriorityQueue.size -= 1
        return temp_data

def emptyQueue(queue):
	"""
	This function returns None if the Queue is empty, more specifically if the front element
	is empty.
	"""
    return queue.front == None

