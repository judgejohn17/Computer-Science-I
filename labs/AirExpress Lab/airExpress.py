#File: airExpress.py
#Name: John J.
#Description: This program works in conjunction with the myPriorityQueue.py and testMyPriorityQueue.py

from myPriorityQueue import *

class Passenger(rit_object):
    __slots__ = ('name', 'priority')
    __types_  = (str, int)

def front(queue):
    """
    This function returns front element of queue
    """
    if emptyQueue(queue):
        raise IndexError("Front from empty queue")
    else:
        return queue.front.data

def main():
    """
    This function is responsible for taking a text file and striping the passenger names and seat
    numbers. It passes this information to myPriorityQueue.py
    """
    imput_file = input("file: ")
    with open(imput_file) as file:
        for line in file:
            line = line.split()
            if len(line) > 2:
                new_passenger = Passenger(line[1], int(line[2]))
                myPriorityQueue.insert(air_express_priority_queue, new_passenger)
            else:
                called_seat = int(line[1])
                print("***Now boarding seat ", called_seat, "***")
                while air_express_priority_queue.front.data.seat >= called_seat:
                    exitied = myPriorityQueue.remove(air_express_priority_queue)
                    print(exitied.name, " boarding seat ", exitied.priority, " successfully.")
        while air_express_priority_queue.front is not None:
            never_exitied = myPriorityQueue.remove(air_express_priority_queue)
            print(never_exitied.name, " was left at the gate.")

