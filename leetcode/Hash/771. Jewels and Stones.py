class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 1. 돌 개수 취합한 딕셔너리 생성
        # 2. 보석을 키로 딕셔너리에서 개수 찾아서 취합
        
        table = collections.defaultdict(int)
        answer = 0
        
        for stone in stones:
            table[stone] += 1
        
        for jewel in jewels:
            answer += table[jewel]
        
        return answer
        
        
        