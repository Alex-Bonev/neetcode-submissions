class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if heights is None: return None

        # we know that it can make it to the pacific either if it is on the border, or it is >= something that can make it to the pacific

        #once we know that, we can do the same thing in the atlantic direction. Everything that works for both, we return.

        #we can make a set where the values are tuples representing the coordinates, and we can simply look for those tuples when going the other way

        pacific = set()

        result = []

        def visitPacific(r, c):
            if (r-1 >= 0 and heights[r][c] <= heights[r-1][c] and (r-1, c) not in pacific):
                pacific.add((r-1, c))
                visitPacific(r-1, c)
            if (r+1 < len(heights) and heights[r][c] <= heights[r+1][c] and (r+1, c) not in pacific):
                pacific.add((r+1, c))
                visitPacific(r+1, c)

            if (c-1 >= 0 and heights[r][c] <= heights[r][c-1] and (r, c-1) not in pacific):
                pacific.add((r, c-1))
                visitPacific(r, c-1)
            if (c+1 < len(heights[0]) and heights[r][c] <= heights[r][c+1] and (r, c+1) not in pacific):
                pacific.add((r, c+1))
                visitPacific(r, c+1)
        
        for c in range(0, len(heights[0])):
            pacific.add((0, c))
            visitPacific(0, c)

        for r in range(1, len(heights)):
            pacific.add((r, 0))
            visitPacific(r, 0)


        atlantic = set()

        def visitAtlantic(r, c):
            if (r-1 >= 0 and heights[r][c] <= heights[r-1][c] and (r-1, c) not in atlantic):
                atlantic.add((r-1, c))
                visitAtlantic(r-1, c)
            if (r+1 < len(heights) and heights[r][c] <= heights[r+1][c] and (r+1, c) not in atlantic):
                atlantic.add((r+1, c))
                visitAtlantic(r+1, c)

            if (c-1 >= 0 and heights[r][c] <= heights[r][c-1] and (r, c-1) not in atlantic):
                atlantic.add((r, c-1))
                visitAtlantic(r, c-1)
            if (c+1 < len(heights[0]) and heights[r][c] <= heights[r][c+1] and (r, c+1) not in atlantic):
                atlantic.add((r, c+1))
                visitAtlantic(r, c+1)

        for c in range(0, len(heights[0])):
            atlantic.add((len(heights)-1, c))
            visitAtlantic(len(heights)-1, c)

        for r in range(0, len(heights)):
            atlantic.add((r, len(heights[0])-1))
            visitAtlantic(r, len(heights[0])-1)

        for coord in pacific:
            if coord in atlantic:
                result.append([coord[0], coord[1]])
        

        return result






