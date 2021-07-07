class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1. 번호에서 사용할 수 있는 알파뱃 목록 딕션너리 생성
        """
        2   a, b, c
        3   d, e, f
        
        위에서 a는 d, e, f를 전부 탐색 해야하고
        b도 마찬가지로 쭉쭉 뻗어나가는 모양새가
        척 보니 dfs
        """
        # 2. digits 길이를 큰 루프
        # 3. 번호마다 사용할 수 있는 알파뱃들은 작은 루프
        # 4. 루프 돌면서 현재 값 저장하고 다음 번호로 넘어가야함 -> dfs
        # 5. 종료 조건 생성 -> 저장한 값의 길이가 digits의 길이와 같으면 종료
        
        """
        제일 첫 번째 dfs에서의 2중 루프의 i가 1이 되었을 때부터는 아예 답을 만들 수 없음
        3번에서 dfs를 뚫고 들어가도 다음 digit은 존재하지 않기 때문임
        따라서 불필요한 연산을 시도하지 않게 해서 최적화를 추가함
        
        dfs실행시 현재의 인덱스와 저장하고 있는 값의 길이가 다르다면 첫번째 dfs를 벗어나기
        시작했으므로 바로바로 종료함
        """
        
        
        if digits == "":
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def dfs(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            if idx != len(path):
                return
            
            for i in range(idx, len(digits)):
                for j in phone[digits[i]]:
                    dfs(i+1, path+j)
                    
        result = []
        dfs(0, '')
        return result
                
