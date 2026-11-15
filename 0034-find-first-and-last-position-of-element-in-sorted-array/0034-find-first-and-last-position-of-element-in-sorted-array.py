class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first_occurrence():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    high = mid - 1

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        def last_occurrence():
            low = 0
            high = len(nums) - 1
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid
                    low = mid + 1

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        return [first_occurrence(), last_occurrence()]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna