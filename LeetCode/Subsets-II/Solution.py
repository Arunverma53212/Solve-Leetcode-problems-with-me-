1
2class Solution:
3    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
4        result = []
5        nums.sort()
6
7        def solve(index, subset):
8            result.append(subset.copy())
9
10            for i in range(index, len(nums)):
11
12                # Skip duplicate elements at the same level
13                if i > index and nums[i] == nums[i - 1]:
14                    continue
15
16                # Choose the current element
17                subset.append(nums[i])
18
19                # Explore further
20                solve(i + 1, subset)
21
22                # Backtrack
23                subset.pop()
24
25        solve(0, [])
26        return result
27
28