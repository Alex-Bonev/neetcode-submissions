class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        m = math.floor((l+r)/2)

        while r > l:
            if nums[l] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m+1
            else:
                return nums[l]
            m = math.floor((l+r)/2)
            # print(f"l {l} | m {m} | r {r}")
        
        return nums[l]
