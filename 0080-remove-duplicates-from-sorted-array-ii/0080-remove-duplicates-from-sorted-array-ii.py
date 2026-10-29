class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        k = 1
        for i in range(2,n):
            if nums[i] != nums[k-1]:
                k+=1
                nums[k] = nums[i]
        return k + 1
        