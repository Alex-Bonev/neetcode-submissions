# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #first, we need to find p or q
        #once we find one of them, we need to check if the other is rooted in a subtree rooted at the first. If so, then the first is the LCA
        #otherwise, we go up one and search in order

        def visit(node):

            if (p.val < node.val and q.val < node.val):
                return visit(node.left)
            elif (p.val > node.val and q.val > node.val):
                return visit(node.right)
            else:
                return node

            return None;
        
        return visit(root)
        