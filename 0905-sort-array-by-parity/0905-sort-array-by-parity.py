class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        k = 0
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 0:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                k = k + 1
        return nums
           

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna