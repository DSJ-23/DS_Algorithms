from DS.binary_tree_library import *

root.left.left.left = Node(-1)
root.left.left.right = Node(2)
root.left.left.left.right = Node(0)

root.right.right.left = Node(10)
root.right.right.right = Node(12)

# print(root)

def post_order(root):
    values = []
    def post_dfs(root):
        if root is None:
            return
        nonlocal values
        post_dfs(root.left)
        post_dfs(root.right)
        values.append(root.value)
    post_dfs(root)
    return values

def pre_order(root):
    values = []
    def pre_dfs(root):
        if root is None:
            return
        nonlocal values
        values.append(root.value)
        pre_dfs(root.left)
        pre_dfs(root.right)
    pre_dfs(root)
    return values

# print(pre_order(root))

def traverse_tree_in_order(root):
    values = []

    def bfs(root):
        if root is None:
            return
        nonlocal values
        bfs(root.left)
        values.append(root.value)
        bfs(root.right)
    bfs(root)
    return values

# print(traverse_tree_in_order(root))


def bfs_traverse(root):
    line = [root]
    while line != []:
        current = line.pop(0)
        if current.left:
            line.append(current.left)
        if current.right:
            line.append(current.right)
        print(current.val)
    return root

def find_minimum(root):
    current = root
    while current.left:
        current = current.left
    return current.val

def min_recur(root):
    if root.left:
        return min_recur(root.left)
    return root.val


