class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        if len(edges) > (n - 1):
            return False
        
        neighbors = {i: [] for i in range(n)}
        for key, value in edges:
            neighbors[key].append(value)
            neighbors[value].append(key)
        
        # from here, we want to run DFS to see if there are any cycles
        # we will keep a log of what we have visited thusfar

        visited = set()


        def dfs(node, parent):
            if node in visited:
                return False
            if neighbors[node] == []:
                return True
            
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n