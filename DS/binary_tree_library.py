from binarytree import Node, tree

root = Node(7)
root.left = Node(3)
root.right = Node(9)

root.left.left = Node(1)
root.left.right = Node(5)

root.left.right.left = Node(4)
root.left.right.right = Node(6)

root.right.right = Node(11)
root.right.left = Node(8)


#      _5__
#    /     \
#   3       8
#  / \     / \
# 1   4   7   9