class Solution: 
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna