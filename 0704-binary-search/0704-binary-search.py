class Solution(object):
    def search(self, nums, target):
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1
   


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna