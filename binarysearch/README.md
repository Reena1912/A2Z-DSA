## Search in sorted array

binary search is an algorithm that finds an element in a sorted space

in this que a target is given and we had to find that element in array and chheck if it is present or not

# approach
so we have used the iterative approach where we have initialized the low at 0 index and high at last index
we found the mid based on the low and high using formula 

mid=(low+high)//2

if target is euall to the mid we simply return its index
if target is greater than mid then we have no use of the left part of the mid, so we eleminate that and move the low pointer to mid+1
if target is smaller than mid then we have no use of the right part so we eliminate that and move the high pointer high=mid-1

if the number is not found then we return -1

## Approach (Easy Explanation)

Binary Search works on a **sorted array**.

Instead of checking every element, we:
1. Find the middle element
2. Compare it with target
3. If equal → return index
4. If target is bigger → search right half
5. If target is smaller → search left half

Repeat until found or search space becomes empty.

## Steps

1. Initialize:
   - low = 0
   - high = n - 1

2. While low <= high:
   - Find mid index
   - Compare nums[mid] with target

3. Return index if found, else return -1

---



- **Lower Bound** → first index where element is **≥ x**
- **Upper Bound** → first index where element is **> x**

---

## Example

Array:
3 5 8 9 15 19  

### Case 1:
x = 8  

Lower Bound → index 2 (value = 8)  
Upper Bound → index 3 (value = 9)

---

### Case 2:
x = 88  

Lower Bound → 6  
Upper Bound → 6  

👉 (Position where it can be inserted at the end)

---

## Approach (Easy Explanation)

We use Binary Search:

### For Lower Bound:
- If `nums[mid] >= x` → store answer and move left
- Else → move right

---

### For Upper Bound:
- If `nums[mid] > x` → store answer and move left
- Else → move right





# Search Insert Position

## Problem
Given a sorted array and a target value, return the index if the target is found.  
If not, return the index where it should be inserted.

---

## Example

### Example 1:
Input:
nums = [1, 3, 5, 6]  
target = 5  

Output:
2  

---

### Example 2:
Input:
nums = [1, 3, 5, 6]  
target = 2  

Output:
1  

---

### Example 3:
Input:
nums = [1, 3, 5, 6]  
target = 7  

Output:
4  

---

## Approach (Easy Explanation)

We use Binary Search.

Instead of finding exact match only, we find:
👉 the first position where element is **greater than or equal to target**

This is also called **Lower Bound**.

---

## Steps

1. Initialize:
   - low = 0
   - high = n - 1
   - ans = n

2. While low <= high:
   - Find mid index
   - If nums[mid] >= target:
       - store mid in ans
       - move left
   - Else:
       - move right

3. Return ans

---