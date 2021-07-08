class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            rv_target = target - v
            idx = bisect.bisect_left(numbers, rv_target, k+1)
            if idx < len(numbers) and numbers[idx] == rv_target:
                return k+1, idx+1
