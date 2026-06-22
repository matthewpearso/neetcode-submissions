# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        current = head
        while current:
            counter += 1
            current = current.next
        
        remove = counter - n

        if counter == n:
            head = head.next
            return head
        
        current = head
        for i in range(counter - 1):
            if i + 1 == remove:
                current.next = current.next.next
                break
            else:
                current = current.next
        
        return head



