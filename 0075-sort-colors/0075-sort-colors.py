class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = 0
        right = len(nums)-1
        while i<=right:
            if nums[i] == 0:
                nums[left],nums[i]= nums[i],nums[left]
                left+=1
                i+=1
            elif nums[i] == 1:
                i+=1
            else:
                nums[i],nums[right] = nums[right],nums[i]
                right-=1
        return nums



        
        


 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna