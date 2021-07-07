class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        dist = collections.defaultdict(int)
        q = [(0, k)]
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    accum = time + w
                    heapq.heappush(q, (accum, v))
        
        if len(dist) == n:
            return max(dist.values())
        return -1
                