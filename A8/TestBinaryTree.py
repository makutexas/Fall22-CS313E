#  File: TestBinaryTree.py

#  Description:

#  Student Name: Mark Chao

#  Student UT EID: mc72239

#  Partner Name: Ben Ton-That

#  Partner UT EID: bbt426

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 10/18/2022

#  Date Last Modified: 10/21/2022

import sys

class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1

class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root == None:
            return None
        elif self.root.lChild == None and self.root.rChild == None:
            return 0
        else:
            min = self.root
            max = self.root
            while min.lChild != None:
                min = min.lChild
            while max.rChild != None:
                max = max.rChild
            return max.data - min.data

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        return self.get_level_helper(self.root, level)

    def get_level_helper(self, aNode, level):
        if aNode == None:
            return []
        elif level == 1:
            return [aNode.data]
        elif level == (self.get_height() + 1 - aNode.get_height()): #Calculates level from height, and compares to desired level
            return [aNode.data] + self.get_level_helper(aNode.lChild, level) + self.get_level_helper(aNode.rChild, level)
        else:
            return self.get_level_helper(aNode.lChild, level) + self.get_level_helper(aNode.rChild, level)

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        list = [] 
        level = 1
        levellist = self.get_level(level)
        height = self.get_height()
        for i in range(height): 
            if levellist == None: 
                break
            if levellist != None: 
                list.append(levellist[0]) 
                level+=1
                levellist = self.get_level(level)
        return(list)
        
    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        return self.sum_leaf_nodes_helper(self.root)

    def sum_leaf_nodes_helper(self, aNode):
        if aNode.lChild == None and aNode.rChild == None:
            return aNode.data
        elif aNode.lChild == None:
            return self.sum_leaf_nodes_helper(aNode.rChild)
        elif aNode.rChild == None:
            return self.sum_leaf_nodes_helper(aNode.lChild)
        else:
            return self.sum_leaf_nodes_helper(aNode.lChild) + self.sum_leaf_nodes_helper(aNode.rChild)

def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", end = '')
    print(t1.left_side_view())
    print("Sum of leaf nodes is: ", end = '')
    print(t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", end = '')
    print(t2.left_side_view())
    print("Sum of leaf nodes is: ", end = '')
    print(t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", end = '')
    print(t3.left_side_view())
    print("Sum of leaf nodes is: ", end = '')
    print(t3.sum_leaf_nodes())
    print("##########################")

    print(t2.root.get_height())

    print(t2.get_level(4))

if __name__ == "__main__":
    main()