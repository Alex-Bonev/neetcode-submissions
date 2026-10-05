"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        visited = {}

        def visit(node: Optional['Node']):
            nonlocal visited

            visited[node] = Node(node.val)


            for i in node.neighbors:
                if i not in visited:
                    visit(i)
                visited[node].neighbors.append(visited[i])
            return visited[node]

        visit(node)

        return visited[node]



