class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        m = []
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        a = sorted(freq,key=freq.get,reverse=True)
        j = 0
        while j<k:
            m.append(a[j])
            j+=1
        return m




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna