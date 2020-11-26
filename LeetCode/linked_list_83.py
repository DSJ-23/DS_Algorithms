class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head