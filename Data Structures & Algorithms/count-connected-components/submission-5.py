class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        neighbors = {i: [] for i in range(n)}
        
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)
        
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in neighbors[node]:
                if nei not in visited:
                    dfs(nei)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count
        



