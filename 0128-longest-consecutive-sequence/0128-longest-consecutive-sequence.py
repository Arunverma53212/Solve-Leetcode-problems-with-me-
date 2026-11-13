class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if (num-1) not in s:
                current_streak = 1
                current = num

                while current+1 in s:
                    current_streak+=1
                    current+=1
                longest = max(longest,current_streak)
        return longest
                

                

     


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna