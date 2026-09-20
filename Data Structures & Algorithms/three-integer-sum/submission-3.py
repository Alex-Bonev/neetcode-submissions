class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        for i, num in enumerate(nums):
            # we are going to anchor one in place
            left = i+1
            right = len(nums)-1
            
            cur = 0
            if (i > 0):
                if num == nums[i-1]:
                    continue

            while left < right and left != i and right != i:
                cur = nums[left] + nums[right] + num
               # print(f"left {nums[left]} | right {nums[right]} | num {num} | cur {cur}")
                if (cur < 0):
                    left += 1
                elif (cur > 0):
                    right -= 1
                else:
                    result.append((nums[left], num, nums[right]))
                    left += 1
                    while (left < right and nums[left] == nums[left-1]):
                        left+=1
                    
                    
        return result
