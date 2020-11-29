
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

    def prepend(self, data): 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def get_node(self, lookup):
        if self.head.data == lookup:
            return self.head
        else:
            current = self.head
            while current.data != lookup:
                current = current.next
            print(current.__dict__)
            return current

    def delete(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        else:
            previous = None
            while cur_node and cur_node.data != key:
                previous = cur_node
                cur_node = cur_node.next
            if cur_node is not None:
                previous.next = cur_node.next
                cur_node.next = None
            else:
                return

    def pop(self, position):
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return
        else:
            previous = None
            count_position = 0
            while cur_node and count_position != position:
                previous = cur_node
                cur_node = cur_node.next
                count_position = count_position + 1

            if cur_node is None:
                return
            
            previous.next = cur_node.next
            cur_node = None

    def length(self):
        cur_node = self.head
        size = 0
        if cur_node is None:
            return 0
        else:
            while cur_node is not None:
                cur_node = cur_node.next
                size += 1
            return size

    def len_recursive(self, node, current_length = 0):
        count = current_length
        cur_node = node
        if cur_node.next != None:
            count += 1
            cur_node = cur_node.next
            return self.len_recursive(cur_node, count)
        else:
            return count +1

    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def reverse(self):
        previous = None
        current = self.head
        next_node = current.next
        if self.head is None:
            return False
        while current is not None:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node
        self.head = previous
        return

    def node_swap(self, node1, node2):
        return


        

linked = LinkedList()
linked.append("A")
linked.append("B")
linked.append('C')
linked.append('D')
# linked.append('akdfjakdfj')

# print(linked.length_recursive(linked.head))

# print(linked.len_recursive(linked.head, current_length=0))

# print('removing')
# linked.pop(2)
# linked.print_list()
linked.reverse()
linked.print_list()



