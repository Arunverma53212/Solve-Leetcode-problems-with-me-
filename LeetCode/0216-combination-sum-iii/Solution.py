class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        nums = []
        result = []

        for i in range(1,10):
            nums.append(i)
        def solve(nums,index,result,subset):
            if len(subset) == k:
                if sum(subset) == n:
                    result.append(subset.copy())
                return

            if index == len(nums):
                return
            
            subset.append(nums[index])
            solve(nums,index+1,result,subset)
            subset.pop()
            solve(nums,index+1,result,subset)
        solve(nums,0,result,[])
        return result

