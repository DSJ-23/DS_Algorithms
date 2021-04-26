class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if self.get_values(head) == self.reverseList(head):
            return True
        return False
    
    def get_values(self, head):
        current = head
        out = []
        while current is not None:
            # out.append(current.val)
            # out.insert(0, current.val)
            current = current.next
        return out
        
    def reverseList(self, head):
        previous = None
        current = head
        next_node = None
        out = []
        if current is None:
            return current
        while current is not None:
            out.insert(0, current.val)
            
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node
        head = previous
        return current