import time

def sort_list(lst):
    """
    This program sorts the list. This is what sets the findFast.py aside from the findSLow.py.
    This also results in a slower program.
    """
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst
  
def find_median(lst):
    """
    This function is responsible for finding the median of the list. It soes this by taking the 
    length of the list. If it is odd it removes the remainder and rounds it down to the nearest 
    intiger. 
    """
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        lower_index = len(lst) // 2
        return int(lst[lower_index] + lst[lower_index + 1]) / 2
 
def find_sum_of_distances(median, lst):
    sum = 0
    for place in lst:
        sum += abs(int(place) - int(median))
    return sum
 
def extract_list():
    """
    This function is responsible for opening the text file thats is used in conjunction with the 
    program. It takes the list and splits each line one by one and returns the new list.
    """
    data = []
    file_name = input('File name: ')
    with open(file_name) as file:
        for line in file:
            data += [int(line.split()[1])]
    return data
 
def main():
    start_time = time.clock()
    lst = extract_list()
    lst = sort_list(lst)
    med = find_median(lst)
    elapsed_time = time.clock() - start_time
    print("Elapsed time is " + str(elapsed_time))
    print('The best location is ' + str(med))
    dist_sum = find_sum_of_distances(med, lst)
    print("Sum of distances is " + str(dist_sum))
 
main()