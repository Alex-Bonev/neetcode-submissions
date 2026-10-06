class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # at each step, we can choose whether or not to rob the house
        # if we DO rob the house, we cannot rob the next. At each point, 
        # the split realities are: rob next house, rob one after it
        memo = {}


        def dfs(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]

        return dfs(0)