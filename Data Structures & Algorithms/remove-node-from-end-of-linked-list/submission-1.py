# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length+=1
        
        cur = head

        if (length-n-1 < 0):
            return head.next
        else:
            for i in range(length-n-1):
                cur = cur.next
        
        if (cur.next):
            if (cur.next.next):
                cur.next = cur.next.next
            else:
                cur.next = None
        
        return head
