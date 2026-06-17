# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next
        count = 1

        while fast != slow:
            if fast.next == None:
                return False
            
            if count % 2 == 0:
                slow = slow.next

            fast = fast.next
            count += 1
        
        return True
                

