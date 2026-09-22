# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        fast = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        while fast.next:
            cur = cur.next
            fast = fast.next
        
        cur.next = cur.next.next

        return head
