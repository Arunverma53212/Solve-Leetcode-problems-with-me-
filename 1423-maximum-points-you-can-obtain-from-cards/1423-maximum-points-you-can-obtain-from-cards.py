class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:

        left_sum = sum(cardPoints[:k])
        max_sum = left_sum

        right = len(cardPoints) - 1

        for i in range(k - 1, -1, -1):

            left_sum -= cardPoints[i]
            left_sum += cardPoints[right]

            max_sum = max(max_sum, left_sum)

            right -= 1

        return max_sum


        


        
        




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna