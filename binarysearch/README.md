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

# 🔍 Find First and Last Position of Element in Sorted Array

## 📌 Problem
Given a sorted array `nums` (non-decreasing order), find the **starting** and **ending position** of a given `target`.

If the target is not found, return: [-1, -1]

## 🧠 Approach

We use **Binary Search twice**:

1. **First Occurrence (Leftmost Index)**
2. **Last Occurrence (Rightmost Index)**

---

## 💡 Key Idea

Instead of stopping when we find the target:

- For **first position** → keep searching **left**
- For **last position** → keep searching **right**

👉 This helps us find the full range of the target.

---

## 🪜 Steps

### 1️⃣ First Position
- Initialize:
  - `low = 0`, `high = n - 1`
  - `first = -1`

- While `low <= high`:
  - Find `mid`
  - If `nums[mid] == target`:
    - store index
    - move left → `high = mid - 1`
  - Else if `nums[mid] < target`:
    - move right → `low = mid + 1`
  - Else:
    - move left → `high = mid - 1`

---

### 2️⃣ Last Position
- Initialize:
  - `low = 0`, `high = n - 1`
  - `last = -1`

- While `low <= high`:
  - Find `mid`
  - If `nums[mid] == target`:
    - store index
    - move right → `low = mid + 1`
  - Else if `nums[mid] < target`:
    - move right → `low = mid + 1`
  - Else:
    - move left → `high = mid - 1`

---
Input: nums = [5,7,7,8,8,10], target = 8  
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6  
Output: [-1,-1]

Input: nums = [], target = 0  
Output: [-1,-1]

⏱️ Complexity
Time: O(log n) (Binary Search twice)
Space: O(1)

🔑 Key Takeaways
Binary Search can be used to find boundaries, not just elements
Do NOT stop when target is found
Use:
Left bias → First occurrence
Right bias → Last occurrence
Works only on sorted arrays
Very common interview pattern

🚀 What I Learned
How to modify binary search logic instead of stopping early
Importance of constraints (O(log n))
Concept of searching for range using two passes
Reusable pattern for many problems


# 🔍 Count Occurrences of Element in Sorted Array

## 📌 Problem
Given a **sorted array**, count the number of times a given element `x` appears.

If the element is not present, return `0`.

---

## 🧠 Approach

We use **Binary Search** to find:

1. **First Occurrence** of `x`
2. **Last Occurrence** of `x`

Then calculate: count = last - first + 1

---

## 💡 Key Idea

Instead of scanning the array:

- Find **first index** where `x` appears  
- Find **last index** where `x` appears  

👉 The difference gives total occurrences

---

## 🪜 Steps

### 1️⃣ First Occurrence
- If `arr[mid] == x`:
  - store index
  - move left → `high = mid - 1`
- If `arr[mid] < x`:
  - move right → `low = mid + 1`
- Else:
  - move left → `high = mid - 1`

---

### 2️⃣ Last Occurrence
- If `arr[mid] == x`:
  - store index
  - move right → `low = mid + 1`
- If `arr[mid] < x`:
  - move right → `low = mid + 1`
- Else:
  - move left → `high = mid - 1`

---

### 3️⃣ Count
- If element not found → return `0`
- Else: count = last - first + 1

# example
Input:
arr = [2, 4, 6, 8, 8, 8, 11, 13]
x = 8

Output:
The number of occurrences is: 3

# 🔍 Search in Rotated Sorted Array
Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

## 📌 Problem
You are given a **sorted array that has been rotated** and a target value.

👉 Your task:
- Find the index of the target  
- If not found, return `-1`

---

## 🧠 What is a Rotated Array?

A rotated array is a sorted array that is shifted.

### Example:Original:
         [1, 2, 3, 4, 5, 6, 7]
Rotated: [4, 5, 6, 7, 1, 2, 3]

In a rotated sorted array, the entire array is no longer fully sorted ,but an important property still holds: in every part of the array you look at, one side will always be sorted. This means either the left portion or the right portion of the array will be in increasing order. That’s the key idea we use to find the target efficiently.

### Why Binary Search Still Works:
In normal binary search, we rely on the entire array being sorted to decide whether to go left or right. But in this case, we adapt it slightly we don't require the whole array to be sorted, just identify which part is sorted in the current range. Once we know which part is sorted, we check if the target lies inside that sorted section. If it does, we discard the other half. If not, we discard the sorted half and search the remaining half. No matter how the array was rotated, the sorted structure on at least one side of any middle point always helps us narrow down where to look next. This lets us avoid scanning the whole array like in brute force, and instead bring down the number of checks to logarithmic time.

1) Start by looking at the middle element of the array.

2) Check if this middle element is the target if yes, return its index immediately.
3) Now figure out which half of the array (left side or right side) is sorted.
4) If the left part is sorted:

   4.1) Check if the target number falls within the range of that sorted part.
   4.2) If it does, discard the right half and continue the search in the left part.
   4.3) If it doesn’t, discard the left half and search in the right side.
5) If the right part is sorted:
   5.1) Do the same check if the target is in that sorted part.
   5.2) If yes, discard the left side and search in the right.
   5.3) If not, discard the right and continue with the left.

6) Repeat this process of eliminating half the array until the target is found or the search space is empty.




# Search Element in Rotated Sorted Array II

Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

## Approach
Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.

Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division)

Check if arr[mid] = target: If it is, return True.

Check if arr[low] = arr[mid] = arr[high]: If this condition is satisfied, we will just increment the low pointer and decrement the high pointer by one step. We will not perform the later steps until this condition is no longer satisfied. So, we will continue to the next iteration from this step.


Identify the sorted half, check where the target is located, and then eliminate one half accordingly:
If arr[low] <= arr[mid]: This condition ensures that the left part is sorted.

If arr[low] <= target && target <= arr[mid]: It signifies that the target is in this sorted half. So, we will eliminate the right half (high = mid-1).

Otherwise, the target does not exist in the sorted half. So, we will eliminate this left half by doing low = mid+1.

Otherwise, if the right half is sorted:
If arr[mid] <= target && target <= arr[high]: It signifies that the target is in this sorted right half. So, we will eliminate the left half (low = mid+1).

Otherwise, the target does not exist in this sorted half. So, we will eliminate this right half by doing high = mid-1.

Once, the ‘mid’ points to the target, we will return True.

This process will be inside a loop and the loop will continue until low crosses high. If no element is found, we will return False.


