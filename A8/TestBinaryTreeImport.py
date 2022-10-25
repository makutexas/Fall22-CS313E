from TestBinaryTree import *

tree = make_tree([98, 5, 6, 8, 76, 48, 19, 83, 86, 62, 56, 57, 30])

tree.print(tree.get_height())

print(tree.left_side_view())

list = [node.data for node in tree.get_level(1)]
print(list)