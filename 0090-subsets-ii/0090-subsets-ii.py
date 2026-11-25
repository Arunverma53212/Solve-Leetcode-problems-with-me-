
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        def solve(index, subset):
            result.append(subset.copy())

            for i in range(index, len(nums)):

                # Skip duplicate elements at the same level
                if i > index and nums[i] == nums[i - 1]:
                    continue

                # Choose the current element
                subset.append(nums[i])

                # Explore further
                solve(i + 1, subset)

                # Backtrack
                subset.pop()

        solve(0, [])
        return result



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna