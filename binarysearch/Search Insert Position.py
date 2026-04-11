#Search Insert Position = Lower Bound
'''nums[mid] < target → go right  
else → store ans and go left '''

#nums = [1, 3, 5, 6]
#target = 7 
# output= 4


def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


# -------- INPUT --------
n = int(input())
nums = list(map(int, input().split()))
target = int(input())

# -------- OUTPUT --------
print(search_insert(nums, target))