# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = head
        r = head.next
        l1 = head

        while r and r.next:
            r = r.next.next
            l = l.next
        
        second = l.next
        l2 = self.reverse(second)
        l.next = None

        current = l1
        while l2:
            l1_temp = current.next
            l2_temp = l2.next
            current.next = l2
            l2 = l2_temp
            current = current.next
            current.next = l1_temp
            current = current.next
        


        
    def reverse(self, head):
        current = head
        prev = None

        while current:
            rest = current.next
            current.next = prev
            prev = current
            current = rest
        
        return prev
        


