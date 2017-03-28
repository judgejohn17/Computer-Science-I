#File: test_debug_hw.py
#Name: John J.
#Description: This program tests my knowledge of debugging...and my patience  
"""
test_debug_hw.py homework for csci141.
"""

#######################################################################
## problem 1 of 2.
#######################################################################
# There is a problem with the is_reverse_of function below.
# Assignment 1:
# 1.1. Develop a suite of tests to properly test the function.
# 1.2. Debug this faulty function to locate and correct the problem.

def is_reverse_of( st1, st2 ):
    """
    is_reverse_of : String String -> Boolean
    is_reverse_of tells if one string is the reverse of another.
    preconditions: st1 and st2 are character strings.
    """
    if len( st1 ) != len( st2 ):
        return False
    i = 0
    j = len( st2 )
    while j > 0:
        if st1[i] != st2[-j]:
            return False
        i += 1
        j -= 1

    return True

def test_is_reverse_of():
    """
    a suite of pass/fail test cases to validate that is_reverse_of works.
    """
    # Complete this test function.
    st1 = 'racecar'
    st2 = 'racecar'
    is_reverse_of( st1, st2 )
    st1 = 'john'
    st2 = 'johnny'
    is_reverse_of( st1, st2 )
    st1 = 'alabama'
    st2 = 'racecar'
    is_reverse_of ( st1, st2 )

# DO NOT CALL YOUR TEST FUNCTIONS HERE. See end of this file for directions.

#######################################################################
## problem 2 of 2.
#######################################################################
# There is a problem with the str_search function below.
# Assignment 2:
# 2.1. Develop a suite of tests to properly test this function.
# 2.2. Debug this faulty function to find and fix the problems.
#      The function is called indirectly by main_search.
#      You can use your test suite and/or main_search for debugging.
#      Initial Hints: search for J, L, or C.
# 2.3. Document your debugging results trying to fix the str_search code.

def str_search( data, target, start, end ):
    """
    str_search : String String NatNum NatNum -> NatNum or NoneType
    Description:
    Search for a target value in a sorted data string.
    The search happens between the start and end indices inclusively.
    This starts searching in the middle. If it finds the target, it is done.
    Otherwise it decides whether to search the first half or the second half.
    preconditions: the data string is in ascending alphanumeric order.
    Parameters:
        data - a string
        target - the target value to find is a single character string e.g. 'Q'
        start - the starting index into the data
        end - the ending index into the data
    Returns:
        index of target in data, if present; otherwise None.
    """

    if start == end:
        return None

    mid_index = ( start + end ) // 2
    mid_value = data[mid_index]
    
    # debug statement prints the data.
    #print( "Searching for", target, ":", data[start:mid_index], 
    #    "*" + str( mid_value ) + "*", data[mid_index+1:end+1] )
    
    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return str_search( data, target, start, mid_index-1 )
    else:
        return str_search( data, target, mid_index, end )

def find_target( data, target ):
    """
    find_target : String String -> NatNum or NoneType
    find_target returns the index of target in data or None if not found.
    Parameters:
        data - a string
        target - the target value to find
    Returns:
        The index of the target element in data, if present, or None.
    """

    return str_search( data, target, 0, len( data ) - 1 )

def makeString():
    """
    makeString : () -> String
    makeString returns a String
    """
    data = ""
    # append characters to make the string
    for num in range( 36, 108, 2 ):
        data += chr( num )
    return data

def main_search():
    """
    main_search : Void -> NoneType
    """

    data = makeString()
    print( "Number of elements: ", len( data ) )

    while True:
        print( "\nData: ", data )
        target = input( "Enter a character to find: " )

        if target == "":
            break
        else:
            index = find_target( data, target )
            print()
            if index != None:
                print( target, "found at index", index )
            else:
                print( target, "not found" )
    # end while

def test_str_search():
    """
    a suite of pass/fail test cases to validate that str_search works.
    """
    # Complete this test function.
    data = 'new york'
    target = 'w'
    start = 0
    end = 7
    str_search(data, target, start, end)
    #data = 'racecar'
    #start = 'e'
    #end = 6
    #str_search(data, target, start, end)
    """
    I left this as a comment because it resulsts in a runtime error because the maximum level of recursion is
    reached.
    """
#######################################################################
# 2.3. Document your debugging results trying to fix the str_search code.
# Enter answers to the questions below inside the triple-quoted string.
"""
	Were you able to completely fix str_search?
        No, I was not able to completely fix str_search.
	If not, explain in detail the cases that still fail.
        Every other case will fail because the str_search function is set up so its starts looking in the middle.
        If the target is an odd number in the string when it goes to look left and right and there may not be 
        somethign to the left or right because it gets to the end or begining of the word.
	What tool(s) did you use?
        I used PyCharm debugger but had next to no idea how to used it. Then I tried to use my knowledge, that didnt 
        work. Probably because I have no idea how to do this. Then I consulted a few friends, none of which had a 
        clue what to do. Then they asked their friends and suddenly we had a web of people in Computer Science. 
        None of which had an idea to do.
	What went well?
        Nothing. Nothing went well. I had to go through each line thinking through the logic and possible test cases 
	What problems did you have?
        Where do I start? Figuring out how to use debugging tools was a huge part of my problem. Figuring out the 
        actual points of error was also a problem 
"""
#######################################################################

if __name__ == "__main__":
    #
    # Run the test functions for problem 1 and problem 2.
    #
    test_is_reverse_of()
    test_str_search()
    #
    main_search()

# After finishing the problems, submit this file to the mycourses dropbox.