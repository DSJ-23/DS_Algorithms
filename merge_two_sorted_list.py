from typing import List

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        first = l1
        second = l2
        cur = -1
    
        result = ListNode(-1, None)
        temp = result
        
        while cur:
            try:
                a = first.val
            except:
                a = None
            try:
                b = second.val
            except:
                b = None
            cur = return_min(a, b)
            if cur is None:
                break
            temp.next = ListNode(cur, None)
            temp = temp.next
            if (first) and(cur == first.val) :
                first = first.next
            elif (second):
                second = second.next
        return(result.next)
    

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        first = l1
        second = l2
        cur = -1
    
        result = ListNode(-1, None)
        
        while cur:
            try:
                a = first.val
            except:
                a = None
            try:
                b = second.val
            except:
                b = None
            cur = return_min(a, b)
            if cur is None:
                break
            result.val = cur
            result.next = ListNode(None,None)
            result = result.next
            if (first) and(cur == first.val) :
                first = first.next
            elif (second):
                second = second.next
        print(result)
        return(result)
    
def return_min(first, second):
    if first and second:
        return min(first, second)
    elif first is None and second is None:
        return None
    elif first is None:
        return second
    return first