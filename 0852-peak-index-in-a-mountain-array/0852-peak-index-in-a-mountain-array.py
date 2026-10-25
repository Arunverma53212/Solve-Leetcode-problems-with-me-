class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx = 0
        low = 1
        high = len(arr)-2

        while low <= high:
            mid = (low+high) // 2
            if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid

            if arr[mid-1] < arr[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1
        
        
            
        
                
