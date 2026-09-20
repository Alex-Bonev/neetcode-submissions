class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m =(l+r) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m+1
            else:
                return nums[l]
            # print(f"l {l} | m {m} | r {r}")
        
        return nums[l]
