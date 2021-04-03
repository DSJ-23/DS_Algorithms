class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l2 is None:
            return l1
        elif l1 is None:
            return l2
        first = l1
        second = l2
        return first
                
        
#         first_head = l1
#         second_head = l2
#         if l1.val <= l2.val:
#             head = l1
#             first_head = l1.next
#         else:
#             head = l2
#             second_head = l2.next
#         current = head
#         while first_head is not None or second_head is not None:
#             if first_head is not None and second_head is not None:
#                 if first_head.val <= second_head.val:
#                     current.next = first_head
#                     first_head = first_head.next
#                     current = first_head.next
#                 else:
#                     current.next = second_head
#                     second_head = second_head.next   
#                     current = second_head.next
#         if first_head is not None:
#             first_head.next = None
#             current.next = first_head
#         elif second_head is not None:
#             second_head.next = None
#             current.next = second_head
#         return head
    
    
     # elif first_head is not None:
     #            first_head.next = None
     #            current.next = first_head
     #        elif second_head is not None:
     #            second_head.next = None
     #            current.next = second_head