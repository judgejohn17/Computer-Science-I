
#File: tower.py
#Name: John J.
#Description: This program solves the Tower of Hanoi Puzzle in conjuction with tower_animate.py, rit_object.py, myNode.py, and myStack.py

from tower_animate import *

def DO_ANIMATION():
    return True

def solve(stacks, numDisks, original, other, final):
    """
    Solve is a recursive function that solves the Tower of Hanoi puzzle. In this function "stacks"
    is the pegs in the physical Tower of Hanoi puzzle. The numDisks stands for the number of disks.
    """
    nMoves = 0
    if numDisks == 0:
        pass
    else:
        nMoves = solve(stacks, numDisks-1, original, final, other)
        temp = top(stacks[original])
        stacks[final] = push(stacks[final], temp)
        stacks[original] = pop(stacks[original])
        animate_move(stacks, original, final)
        nMoves += 1
        nMoves += solve(stacks, numDisks-1, other, original, final)
    return nMoves

def movePile(stackContents, fromPile, toPile):
    """
    The movePile function is responsible for actauly moving the disks from the three different
    stacks. This is done by pop() the top disk from each stack and putting it on a new stack.
    """

    if stackContents[fromPile].data > stackContents[toPile].data:
        stackContents[toPile] = push(stackContents[fromPile].datastackContents[toPile])
        stackContents[fromPile] = pop(stackContents[fromPile])
    else:
        raise('Cannot place disk on one that is larger than it.')
    return stackContents

def init_puzzle(disks):
    """
    The init_puzzle function initializes the pegs by first establishing there is now disks on any
    of the pegs and then it will put however many disks the user prompts the computer to put on the
    starting peg.
    """

    return_list = [None, None, None]
    while disks > 0:
        return_list[0] = push(return_list[0], disks)
        disks -= 1
    return return_list

def main():
    disks = int(input('How high a tower to start with: '))
    if disks < 1:
        raise ValueError('Disks must be greater than 0')
    if DO_ANIMATION():
        animate_init(disks)
    towers_list = init_puzzle(disks)
    moves = solve(towers_list, disks, 0, 1, 2)
    print('The tower of Hanoi puzzle with ', disks, " disks is solved in ", moves, " moves.")
    input("Press enter to quit")
    if DO_ANIMATION():
        animate_finish()
main()