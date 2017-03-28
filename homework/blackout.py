#File: blackout.py
#Name: John J.
#Description: This program fufills the blackout problem lab
def compute(side):
    if not side[0].isdigit():
        return None
    prevChar = ""
    for currentChar in side:
        if not currentChar.isdigit() and not prevChar.isdigit():
            return None
        else:
            prevChar = currentChar
    val = 0
    nextVal = 0
    operation= ""
    for i in side:
        if i.isdigit():
            if operation== "":
                if val == 0:
                    val = int(i)
                else:
                    val = int(str(val) + i)
            else:
                if nextVal == 0:
                    nextVal = int(i)
                else:
                    nextVal = int(str(nextVal) + i)
        else:
            if operation== "":
                operation= i
            else:
                val = doMath(val, nextVal, operation)
                nextVal = 0
                operation= i
    return doMath(val, nextVal, operation)
    """The compute function goes through the string and compare the each character to the previous
    character. It decides wether it is looking at a digit or an operation. It will take the digit 
    from the string and create an intiger out of it and culmintaes the values for the intigers by 
    calling it "val". However, it will not simply add two intigers, instead it turns multiple
    intigers in a row into a string and reverts that string back into an intger. Then when it 
    reaches an operation it goes to the doMath function to find what the operation is. Then the 
    intigers to the right of the function are defined as nextVal until it can find the value of the 
    intigers(operation)nextVal."""

def doMath(val, nextVal, operation):
    if operation== "+":
        return nextVal + val
    if operation== "-":
        return val - nextVal
    if operation== "/":
        if nextVal == 0:
            return None
        else:
            return val/nextVal
    if operation== "*" or operation== "x":
        return val*nextVal
    """The doMath function, for lack of a better term, does math. It takes the character for 
    mathmatical operations (+,-,/,(x or *)) and turns them into an actual operation by returning
    the operation with 0's on either side (for addition and subtraction). For multiplication and 
    division it returns the operation with val and nextVal on either side"""

def evaluate(equation):
    index = equation.find('=')
    part1 = equation[0:index]
    part2 = equation[index+1:len(equation)]
    side1 = compute(part1)
    side2 = compute(part2)
    if side1 == side2:
        return True
    else:
        return False
    """The evaluate function takes the string of the blackout equation by breaking it in two at the
    '=' character. It then takes the two sides and calls the compute function to, well, compute the 
    value of the sides. It then compares the value for the left side and right side and compares 
    them. If they are equal the function returns "True", if not, it returns "False"."""

def solve(equation):
    solution = ""
    for i in range(0,len(equation)):
        for j in range(i+1,len(equation)):
            if equation[i] == "=":
                pass
            elif equation[j] == "=":
                pass
            else:
                solution = equation[:i] + equation[i+1:j]+ equation[j+1:]
                if evaluate(solution) == True:
                    return solution

    """The solve function is responsible for actually blacking out characters. it does this by 
    using the variables i and j. It starts with i, being the first character on the left. J is 
    one more than i. The function goes through by adding one to j and running through the string
    looking for the solution. Once the range for j is found the function then moves i by 1 and 
    runs for the range of j until the function finds the solution to the black out puzzle."""

def main():
    side = str
    print("22-11x4=", compute("22-11x4"), " (expect 44)")
    print("+11x4=", compute("+11x4"), " (expect None)")
    print("22-11x4 ?= 7x5+9", evaluate("22-11x4=7x5+9"), "(expect True)")
    print("solving 288/24x6=18x13x8 :", solve("288/24x6=18x13x8"))

main()