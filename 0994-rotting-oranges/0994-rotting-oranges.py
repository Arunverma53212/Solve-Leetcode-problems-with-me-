import copy
from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = copy.deepcopy(grid)

        fresh = 0
        que = deque()

        for i in range(rows):
            for j in range(cols):
                if grid_copy[i][j]==2:
                    que.append((i,j))

                elif grid_copy[i][j]==1:
                    fresh+=1
        minutes = 0
        while len(que)!=0 and fresh>0:
            minutes+=1
            total_rotten = len(que)
            for _ in range(total_rotten):
                i,j = que.popleft()

                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_i,new_j = x+i,y+j

                    
                    if new_i < 0 or new_i == rows or new_j < 0  or new_j == cols:
                        continue
                    if grid_copy[new_i][new_j] == 2 or grid_copy[new_i][new_j]==0:
                        continue
                    
                    fresh-=1
                    grid_copy[new_i][new_j] = 2
                    que.append((new_i,new_j))
        if fresh > 0:
            return -1
        return minutes

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna