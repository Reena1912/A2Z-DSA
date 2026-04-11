# Medium que
# Rotate Matrix by 90 Degrees

## Problem
Given a square matrix (n x n), rotate it 90 degrees clockwise.

---

## Approach (Easy Explanation)

We do this in **2 simple steps** instead of rotating directly.

### Step 1: Transpose the matrix
Convert rows into columns.

Example:

Before:

1 2 3  
4 5 6  
7 8 9  

After transpose:

1 4 7  
2 5 8  
3 6 9  

---

### Step 2: Reverse each row
Now reverse every row.

After reversing:
7 4 1  
8 5 2  
9 6 3  

---

## Final Result
We get the matrix rotated by 90 degrees clockwise.

---

## Trick to Remember
Transpose + Reverse = 90° rotation

---

## Time Complexity
O(n^2)

## Space Complexity
O(1)

---

## What I Learned
- How to use transpose in matrices
- How reversing helps in rotation
- How to solve problems in-place (without extra space)

## Code Explanation

- Used nested loops to transpose the matrix by swapping elements across diagonal
- Used reverse() to flip each row
- Printed the final rotated matrix