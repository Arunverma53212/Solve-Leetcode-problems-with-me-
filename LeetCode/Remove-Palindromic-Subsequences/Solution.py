1class Solution:
2    def removePalindromeSub(self, s: str) -> int:
3        if s == "":
4            return 0
5
6        if s == s[::-1]:
7            return 1
8
9        return 2