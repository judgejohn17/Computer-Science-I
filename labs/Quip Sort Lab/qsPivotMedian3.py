"""
file: qsPivotMedian3.py
version: python3
author: Sean Strout
author: John Judge
purpose: Implementation of the quick-sort algorithm (not in-place).  The 
    pivot is chosen always to be the median-of-3 (the median of
    the first, middle and last values)
"""

import testSorts        # run (for individual test run)

def medianOf3(lst):
    """
    From a lst of unordered data, find and return the the median value from
    the first, middle and last values.
    """
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[0]
        else:
            return lst[1]
    elif len(lst) == 3:
        if lst[0] < lst[1] and lst [1] < lst[2]:
            return lst[1]
        if lst[0] > lst[1] and lst[0] < lst[2]:
            return lst[0]
        else:
            return lst[2]
    else:
        first = lst[0]
        last = lst[len(lst)-1]
        middle = lst[len(lst)//2]
        if first < last:
            if first < middle:
                return first
            else:
                return middle
        elif last < middle:
            return last
        else:
            return middle

    
def quickSort(lst):
    """
    quickSort: List(lst) -> List(result)
        Where the return 'result' is a totally ordered 'lst'.
        It uses the median-of-3 to select the pivot

    e.g.  quickSort([1,8,5,3,4]) == [1,3,4,5,8]
    """
    if len(lst) == 0:
      return list()
      #If lst is blank return a blank list
    else:
        pivot = medianOf3(lst)
        less, same, more = partition(pivot, lst)
        return quickSort(less) + same + quickSort(more)

def partition( pivot, lst ):
    """
    partition: pivot (element in lst) * List(lst) -> 
        tuple(List(less), List(same, List(more))).  
    Where:
        List(Less) has values less than the pivot
        List(same) has pivot value/s, and
        List(more) has values greater than the pivot
    e.g. partition(5, [11,4,7,2,5,9,3]) == [4,2,3], [5], [11,7,9]
    """
    less, same, more = list(), list(), list()
    for val in lst:
        if val < pivot:
            less.append(val)
        elif val > pivot:
            more.append(val)
        else:
            same.append(val)
    return less, same, more
   
if __name__ == "__main__":
    testSorts.run('qsPivotMedian3')