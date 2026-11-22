from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        que = deque()
        visited = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        distance = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==0:
                    que.append([i,j,0])
                    visited[i][j] = 1
        

        while len(que)!=0:
            i,j,d = que.popleft()
            distance[i][j]=d 

            for x , y in [(1,0),(0,-1),(0,1),(-1,0)]:
                new_i,new_j = x+i,j+y

                if new_i < 0 or new_i >= len(mat) or new_j < 0 or new_j >= len(mat[0]):
                    continue
                
                if visited[new_i][new_j]==1:
                    continue
                
                que.append([new_i,new_j,d+1])
                visited[new_i][new_j] = 1
        return distance

            


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna