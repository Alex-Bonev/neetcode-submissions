# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head

        prev = head
        curr = head.next
        head.next = None
        n = True
        while n:
            n = curr.next
            curr.next = prev
            prev = curr
            if (n):
                curr = n

        return curr
