def getFloorAndCeil(arr, x):
    n = len(arr)
    
    # Floor
    floor = -1
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] <= x:
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    
    # Ceil
    ceil = -1
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] >= x:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    
    return floor, ceil



arr = list(map(int, input("Enter sorted array elements: ").split()))
x = int(input("Enter target value: "))


floor, ceil = getFloorAndCeil(arr, x)

print("Floor:", floor)
print("Ceil:", ceil)