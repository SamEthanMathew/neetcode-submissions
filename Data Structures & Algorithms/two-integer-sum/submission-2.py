class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    return [i,j]
        