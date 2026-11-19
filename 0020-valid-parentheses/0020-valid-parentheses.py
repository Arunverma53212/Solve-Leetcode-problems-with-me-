class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for bracket in s:
            if bracket == "("  or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else:
                if len(stack )==0:
                    return False
                ch = stack.pop()
                if (bracket == ")" and ch == "(" ) or (bracket == "]" and ch == "[") or (bracket == "}" and ch == "{"):
                    continue
                else:
                    return False
        return len(stack) == 0




        
             




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna