# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        mid_i = 0
        while (fast and fast.next):
            slow = slow.next
            mid_i += 1
            fast = fast.next.next
        
        if not fast:
            mid_i -= 1

        cur = head

        while mid_i>=0:
            
            next_cur = cur.next

            tail = slow
            for i in range(mid_i):
                tail = tail.next
            cur.next = tail
            tail.next = next_cur
            mid_i -= 1
            
            cur = next_cur
        tail.next = None
        
        


        