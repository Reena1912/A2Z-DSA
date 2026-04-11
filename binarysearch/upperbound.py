#arr[index] > x
class Solution:
    def lowerBound(self,nums,x):
        
        low=0
        high=len(nums)-1
        ans=len(nums)
        
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid] > x:
                ans=mid
                high= mid-1
            else:
                low= mid+1
        return ans
    
    
#input
nums = [3, 5, 8, 9, 15, 19]
x = 88

#function call
obj= Solution()
result= obj.lowerBound(nums, x)

#output
print("The upper bound is the index:", result)
        
        