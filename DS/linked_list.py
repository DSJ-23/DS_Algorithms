
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self, all=False):
        node = self.head
        while node is not None:
            if all is False:
                print(node.data)
            else:
                print(node.__dict__)
            node = node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        last_node.next = new_node


linked = LinkedList()
linked.append("A")
linked.append("B")
linked.print_list(all=True)

