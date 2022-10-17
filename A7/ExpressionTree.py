#  File: ExpressionTree.py

#  Description: ExpressionTree.py creates a binary tree from an infix expression and evaluates the expression. Also can print prefix and post fix expressions. 

#  Student Name: Mark Chao  

#  Student UT EID: mc72239

#  Partner Name: Ben Ton-That

#  Partner UT EID: bbt426

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 10/13/2022

#  Date Last Modified: 10/16/2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        nodeStack = Stack()
        self.root = Node()
        currentNode = self.root
        for chr in expr:
            if chr == "(": #1
                currentNode.lChild = Node(chr)
                nodeStack.push(currentNode)
                currentNode = currentNode.lChild
            elif chr in operators: #2
                currentNode.data = chr
                nodeStack.push(currentNode)
                currentNode.rChild = Node()
                currentNode = currentNode.rChild
            elif chr == ")": #4
                if nodeStack.is_empty() == False:
                    currentNode = nodeStack.pop()
            else: #3
                currentNode.data = chr
                currentNode = nodeStack.pop()
                
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.data in operators:
            if aNode.data == "+":
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            elif aNode.data == "-":
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            elif aNode.data == "*":
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            elif aNode.data == "/":
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            elif aNode.data == "//":
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            elif aNode.data == "%":
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            elif aNode.data == "**":
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        else:
            return float(aNode.data)
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if (aNode != None): 
            print(aNode.data, end = " ") 
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if (aNode != None): 
            self.post_order(aNode.lChild)
            self.post_order(aNode.rChild)
            print(aNode.data, end = " ") 
# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    # line = sys.stdin.readline()
    # expr = line.strip()
    
    expr = "((8+3)*(7-2))" #REMOVE THIS LINE WHEN DONE TESTING

    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", end = " ")
    print(tree.pre_order(tree.root))

    # # get the postfix version of the expression and print
    print("Postfix Expression:", end = " ")
    print(tree.post_order(tree.root))

if __name__ == "__main__":
    main()
