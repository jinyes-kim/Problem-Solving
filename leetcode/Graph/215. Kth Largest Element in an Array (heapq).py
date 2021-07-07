class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)


	#한 줄 풀이
	#return heapq.nlargest(k, nums)[-1]