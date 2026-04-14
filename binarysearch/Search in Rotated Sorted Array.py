#Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
# The array is rotated at some pivot point that is unknown.
# Find the index at which k is present and if k is not present return -1.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        low=0
        high = n-1

        while low<= high:
            mid= (low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low]<=target< nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]< target <= nums[high]:
                    low= mid+1
                else:
                    high= mid -1
        return -1