# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        vals = [head.val]
        curr = head
        while curr.next:
            curr = curr.next
            vals.append(curr.val)
        
        curr = head
        curr.val = vals[-1]
        i = -2
        while curr.next:
            curr = curr.next
            curr.val = vals[i]
            i -= 1
        
        return head
