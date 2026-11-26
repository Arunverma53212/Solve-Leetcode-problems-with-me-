from collections import deque
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
            
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for i in range(cols)]for i in range(rows)]
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or   r == rows-1 or c == cols-1:
                    if  grid[r][c] == 1:
                            que.append((r,c))
                            visited[r][c]=1
        while len(que)!=0:
            i,j = que.popleft()
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i,new_j = x+i,y+j

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j]==0:
                    continue
                if visited[new_i][new_j] == 1:
                    continue
                que.append((new_i, new_j))
                visited[new_i][new_j]=1
        count=0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==0 and grid[i][j]==1:
                    count+=1
        return count




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna