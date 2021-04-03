class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current = head
        visited = []
        done = False
        while done == False:
            if current.val not in visited:
                visited.append(current.val)
            else:
                done = True
                return visited.index(current.val)
            current = current.next
         