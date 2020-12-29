from DS.binary_tree_library import *

#iterative in order
# videos que faltan trees
# two extra mediums 
# tabular los que faltan del study guide y hacer faciles

def traverse_tree_in_order(root):
    values = []

    def bfs(root):
        if root is None:
            return
        nonlocal values
        print(root.value)
        print(values)
        bfs(root.left)
        values.append(root.value)
        bfs(root.right)
    bfs(root)
    return values

# print(root)
# print(traverse_tree_in_order(root))

def in_order_iterative(root):
    line = [root]
    values = []
    current = root
    while line != []:
        if current is not None:
            line.append(current)
            current = current.left 
        else:
            current = line.pop()
            values.append(current.value)
            current = current.right
    return values

print(root)
print(in_order_iterative(root))


