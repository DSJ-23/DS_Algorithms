# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        keys = []
        while current is not None:
            if current.next:
                if current.val == current.next.val:
                    keys.append(current.val)
            current = current.next
        print(keys)
        return head
    
    def delete(self, key, head):
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
    