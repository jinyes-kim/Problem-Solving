class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
	"""
	순차 탐색은 아닌데, 뭔가 패턴이 보인다면 힙으로 정렬해보기
	"""

	heap = []
        for man in people:
            heapq.heappush(heap, (-man[0], man[1]))
        
        result = []
        while heap:
            man = heapq.heappop(heap)
            result.insert(man[1], [-man[0], man[1]])
        
        return result
       	