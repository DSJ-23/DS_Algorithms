class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None:
            return False
        
        if head.next is None:
            return False
        
        hare = head
        if hare.next is None or hare.next.next is None:
            return False
        else:
            hare = hare.next.next
        
        turtle = head
    
        while True:
            
            if hare == turtle:
                return True
            if hare.next and hare.next.next:
                hare = hare.next.next
            else:
                break
            
            if turtle.next:
                turtle = turtle.next
            else:
                break
            
        return False



class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        hare = head
        
        if hare.next is None or hare.next.next is None:
            return False
        else:
            hare = hare.next.next
        
        
        turtle = head
        while hare.next and hare.next.next:
            if hare == turtle:
                return True
            hare = hare.next.next
            turtle = turtle.next
        return False