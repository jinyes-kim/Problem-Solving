class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        value = 1
        for i in range(len(nums)):
            result.append(value)
            value *= nums[i]
        
        value = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= value
            value *= nums[j]

        return result
