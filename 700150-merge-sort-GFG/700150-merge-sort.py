class Solution:
    def mergeSort(self, arr, l, r):

        def merge_array(arr1, arr2):
            result = []
            i, j = 0, 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1

            while i < len(arr1):
                result.append(arr1[i])
                i += 1

            while j < len(arr2):
                result.append(arr2[j])
                j += 1

            return result

        def merge(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge(arr[:mid])
            right = merge(arr[mid:])

            return merge_array(left, right)

        arr[l:r+1] = merge(arr[l:r+1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna