class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def solve(result,subset):
            if len(subset) == len(nums):
                result.append(subset.copy())
                return 
            
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    solve(result,subset)
                    subset.pop()

        solve(result,[])
        return result
