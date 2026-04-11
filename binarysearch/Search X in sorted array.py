class Solution:
    def search(self, nums, target):
        n= len(nums)
        low= 0
        high = n-1
        
        while low<=high:
            mid= (low+high)//2
            
            if target==nums[mid]:
                return mid
            elif target > nums[mid]:
                low= mid+1
            else:
                high = mid-1
        return -1
    
#input
n= int(input())
nums= list(map(int,input().split()))
target= int(input())

#function call
obj=Solution()
result= obj.search( nums, target)

#output
print(result)