class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for man in people:
            heapq.heappush(heap, (-man[0], man[1]))
        
        result = []
        while heap:
            man = heapq.heappop(heap)
            result.insert(man[1], [-man[0], man[1]])
        
        return result
        