class Solution:
    def dfs(self, adj):
        # code here
        visited = [0]*len(adj)
        result = []
        
        def solve(node,visited,result):
            visited[node]=1
            result.append(node)
            
            for n in adj[node]:
                if visited[n]==0:
                    solve(n,visited,result)
        solve(0,visited,result)
        return result
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna