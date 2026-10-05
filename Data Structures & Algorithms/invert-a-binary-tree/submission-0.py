# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None

        root2 = TreeNode(root.val)

        def visit (node: Optional[TreeNode], node2: Optional[TreeNode]):
            
            if (node.right):
                node2.left = TreeNode(node.right.val)
                visit(node.right, node2.left)
            if (node.left):
                node2.right = TreeNode(node.left.val)
                visit(node.left, node2.right)
        
        visit(root, root2)
        return root2
            


            