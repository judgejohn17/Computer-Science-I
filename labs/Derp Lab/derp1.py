"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates preorder expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Sean Strout (sps@cs.rit.edu)

Author: John J. Judge
"""

from derp_node import *
    
##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From an infix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    if len(tokens)== 0:
        return None
    nextToken = tokens.pop()
    if nextToken.isdigit():
        return ('literal', nextToken)
    elif nextToken == "+":
        return ('add', parse( tokens ), parse( tokens ))
    elif nextToken == "-":
        return ('sub', parse( tokens ), parse( tokens ))
    elif nextToken == "*":
        return ('mul', parse( tokens ), parse( tokens ))
    elif nextToken == "//":
        return ('div', parse( tokens ), parse( tokens ))
    else:
        return ('variable', nextToken )

            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    
    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
    elif isinstance(node, MultiplyNode):
        return "("+infix(node.left) + "*" + infix(node.right)+")"
    elif isinstance(node, DivideNode):
        return "("+infix(node.left)+ "//" +infix(node.right)+")"
    elif isinstance(node, AddNode):
        return "("+infix(node.left) + "+" + infix(node.right) +")"
    elif isinstance(node, SubtractNode):
        return "("+infix(node.left) + " - " + infix(node.right) +")"
    
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    
    if isinstance(node, LiteralNode):
        return int(node.val)
    elif isinstance(node, VariableNode):
        return int(symTbl[node.name])
    elif isinstance(node, MultiplyNode):
        return evaluate(node.left, symTbl) * evaluate(node.right, symTbl)
    elif isinstance(node, DivideNode):
        return evaluate(node.left, symTbl) // evaluate(node.right, symTbl)
    elif isinstance(node, AddNode):
        return evaluate(node.left, symTbl) + evaluate(node.right, symTbl)
    elif isinstance(node, SubtractNode):
        return evaluate(node.left, symTbl) - evaluate(node.right, symTbl)
    
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    symTbl = dict()
    with open(inFile) as file:
        for line in file:
            line = line.split()
            print(str(line[0]) + " => " + str(line[1]))
            symTbl[line[0]] = line[1]

    print("Herp, enter prefix expressions, e.g.: + 10 20 (RETURN to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        prefix_vals = prefixExp.split()
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        print("My list is: ", prefix_vals)
        root = parse(prefix_vals)
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_vals = infix(root)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:",infix_vals)
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        int_result = int(evaluate(root, symTbl))
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", int_result)
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
