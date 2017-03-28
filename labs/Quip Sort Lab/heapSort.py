"""
file: heapSort.py
version: python3
author: Sean Strout
author: John Judge
purpose: Implementation of the heapsort algorithm, not
    in-place, (lst is unmodified and a new sorted one is returned)
"""

import heapq  # mkHeap (for adding/removing from heap)
import testSorts    # run (for individual test run)

def heapSort(lst):
    """
    heapSort(List(Orderable)) -> List(Ordered)
        performs a heapsort on 'lst' returning a new sorted list
    Postcondition: the argument lst is not modified
    """
    newlst = []
    heap = []
    i = 0
    # use heapPush to push the item onto heap
    while (i<len(lst)):
        heapq.heappush(heap, lst[i])
        i += 1
    # use heapPop to pop the items off one by one into a new list (which is sorted)
    i = 0
    while i < len(lst):
        newlst.append(heapq.heappop(heap))
        i += 1
    return newlst

if __name__ == "__main__":
    testSorts.run('heapSort')