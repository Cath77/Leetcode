from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        results = []
        nums.sort()

        for a in range(len(nums)):
            if target >= 0 and nums[a] > target:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            for d in range (len(nums) - 1, a + 2, -1):
                if d < len(nums) - 1 and nums[d] == nums[d + 1]:
                    continue
            
                b = a + 1
                c = d - 1
                while b < c:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum > target:
                        c -= 1
                    elif sum < target:
                        b += 1
                    else:
                        results.append([nums[a], nums[b], nums[c], nums[d]])
                        while b < c and nums[b] == nums[b + 1]:
                            b += 1
                        while b < c and nums[c] == nums[c - 1]:
                            c -= 1
                        
                        b += 1
                        c -= 1

        return results
    

print(Solution().fourSum([-3,-1,0,2,4,5], 2))