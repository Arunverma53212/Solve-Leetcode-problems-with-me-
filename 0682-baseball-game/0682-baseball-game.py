class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            try:
                res.append(int(operations[i]))
            except ValueError:
                if operations[i] == "+":
                    res.append(res[-2] + res[-1])
                elif operations[i] == "D":
                    res.append(res[-1] * 2)
                elif operations[i] == "C":
                    res.pop()  
        return sum(res)


 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna