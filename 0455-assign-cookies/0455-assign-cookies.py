class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        ans = 0
        for child in g:
            for j in range(len(s)):
                if s[j] >= child:
                    ans+=1
                    s[j] = 0
                    break
        return ans
                
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna