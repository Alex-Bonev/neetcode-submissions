# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        result = []

        stack = [root]

        while len(stack) > 0:
            layer = []
            for i in range(0, len(stack)):
                node = stack.pop(0)
                layer.append(node.val)
                if node.left is not None: stack.append(node.left)
                if node.right is not None: stack.append(node.right)
            result.append(layer)

        return result
