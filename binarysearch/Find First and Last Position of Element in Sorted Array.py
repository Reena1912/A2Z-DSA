class Solution:
    def searchRange(self, nums, target):
        
        def firstPosition():
            low, high = 0, len(nums) - 1
            first = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    first = mid
                    high = mid - 1   # move left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return first
        
        def lastPosition():
            low, high = 0, len(nums) - 1
            last = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    last = mid
                    low = mid + 1   # move right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return last
        
        return [firstPosition(), lastPosition()]