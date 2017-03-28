"""
file: quipSort.py
version: python3
author: Sean Strout
author: John Judge
purpose: Implementation of the quicheSort algorithm (not in place),
    It first uses quickSort, using the median-of-3 pivot, until it
    reaches a recursion limit bounded by int(math.log(N,2)).
    Here, N is the length of the initial list to sort.
    Once it reaches that depth limit, it switches to using heapSort instead of
    quicksort.
"""

import heapSort             # heapSort
import math                 # log2 (for quicksort depth limit)
import testSorts            # run (for individual test run)

def quipSortRec(lst, limit, less, same, more, pivot, i):
    """
    A non in-place, depth limited quickSort, using median-of-3 pivot.
    Once the limit drops to 0, it uses heapSort instead.
    """
    if limit == 0:
        heapSort.heapSort(lst)
    else:
        if lst[i] < pivot:
            less.append(lst[i])
        elif lst[i] > pivot:
            more.append(lst[i])
        else:
            same.append(lst[i])
        quipSortRec(lst, limit-1, less, same, more, pivot, i+1)
    return lst
    
    """
    Test cases if list is 3 or less elements
    """
    """
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        if lst[0] < lst[1]:
            pivot = lst[0]
        else:
            pivot = lst[1]
    elif len(lst) == 3:
        if lst[0] < lst[1] and lst [1] < lst[2]:
            pivot = lst[1]
        if lst[0] > lst[1] and lst[0] < lst[2]:
            pivot = lst[0]
        else:
            pivot = lst[2]
    """
    """
    If the list is 4 elements or more
    """
    """
    else:
        first = lst[0]
        last = lst[len(lst)-1]
        middle = lst[len(lst)//2]
        if first < last:
            if first < middle:
                pivot = first
            else:
                pivot = middle
        elif last < middle:
            pivot = last
        else:
            pivot = middle
    less, same, more = list(), list(), list()
    if limit > 0:
        if val < pivot:
            less.append(val)
        elif val > pivot:
            more.append(val)
        else:
            same.append(val)
        lst = less + same + more
        quipSortRec(lst, limit-1)
    else:
        heapSort.heapSort(lst)
    """

def quipSort(lst):
    """
    The main routine called to do the sort.  It should call the
    recursive routine with the correct values in order to perform
    the sort
    """
    i = 0
    first = lst[0]
    last = lst[len(lst)-1]
    middle = lst[len(lst)//2]
    if first < last:
        if first < middle:
            pivot = first
        else:
            pivot = middle
    elif last < middle:
        pivot = last
    else:
        pivot = middle
    less, same, more = list(), list(), list()
    N = len(lst)
    limit = int(math.log(N,2))
    quipSortRec(lst, limit, less, same, more, pivot, i)

if __name__ == "__main__":
    testSorts.run('quipSort')