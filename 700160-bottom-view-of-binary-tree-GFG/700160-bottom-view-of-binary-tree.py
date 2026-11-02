from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
    
        q = deque([(root, 0)])
        ans = {}
    
        while q:
            node, line = q.popleft()
    
            ans[line] = node.data
    
            if node.left:
                q.append((node.left, line - 1))
    
            if node.right:
                q.append((node.right, line + 1))
    
        return [ans[key] for key in sorted(ans)]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna