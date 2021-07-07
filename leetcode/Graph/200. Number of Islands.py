class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. 범위 확인
        # 2. 현재 위치 초기화
        # 3. 현재 위치에서 동서남북 반복
        # 4. 1~3 프로세스 반복하면서 루틴마다 += 1
        
        def dfs(i, j):
            if not ( (0 <= i < len(grid)) and (0 <= j < len(grid[0]))) or grid[i][j] != '1':
                return
            
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    answer += 1
        
        return answer
            
            
            
        
