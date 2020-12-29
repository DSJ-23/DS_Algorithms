from DS.binary_tree_library import *
from binary_tree_asc import pre_order, traverse_tree_in_order, post_order

tree = Node(1)

tree.left= Node(2)
tree.left.left = Node(4)
tree.left.right = Node(5)

tree.right = Node(3)

tree.right.left = Node(6)
tree.right.right = Node(7)


second = Node(1)
second.left = Node(2)
second.left.left = Node(4)
second.left.right = Node(5)

second.right = Node(3)

print(post_order(second))

