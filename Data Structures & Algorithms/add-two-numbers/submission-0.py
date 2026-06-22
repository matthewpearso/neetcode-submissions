# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        m = l1
        n = l2
        mag = 1
        while m or n:
            if m:
                sum1 += m.val * mag
                m = m.next
            if n: 
                sum2 += n.val * mag
                n = n.next
            mag = mag * 10
        
        output = sum1 + sum2
        string = str(output)
        reverse = string[::-1]

        head = ListNode(int(reverse[0]))
        current = head
        for i in range(1, len(reverse)):
            current.next = ListNode(int(reverse[i]))
            current = current.next
        
        return head
            

