class Solution:
    def stringsorting(self,s):
        s1 = list(s)
        s1.sort()
        return ''.join(s1)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for s in strs:
            key = self.stringsorting(s)
            if key in freq:
                freq[key].append(s)
            else:
                freq[key] = [s]
        return list(freq.values())
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna