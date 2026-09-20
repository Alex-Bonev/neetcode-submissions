# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # first, lets find smallest

        #then, we can just count up to try and find the next smallest
        ans = -1
        
        steps = k

        def dfs(node):
            nonlocal steps, ans

            if not node:
                return
            
            dfs(node.left)
            if (steps == 0):
                return
            steps -= 1
            if (steps == 0):
                ans = node.val
            else:
                dfs(node.right)
        
        dfs(root)

        return ans

        