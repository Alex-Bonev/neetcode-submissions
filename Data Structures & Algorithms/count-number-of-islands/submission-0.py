class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            nonlocal grid

            
            if (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "1"):
                grid[row][col] = "0"    
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)

            return

        islands = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
        return islands
        