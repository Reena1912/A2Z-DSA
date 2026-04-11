# Problem: Rotate Matrix by 90 Degrees
# Given an n x n matrix, rotate it 90 degrees clockwise.
#
# Example:
# Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
#
# Output:
# 7 4 1
# 8 5 2
# 9 6 3


# Problem: Rotate Image (Leetcode 48)
# Approach: Transpose + Reverse
# Time: O(n^2)
# Space: O(1)

def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n): #❌ If you did j = 0 You would swap:(0,1) ↔ (1,0) AND again (1,0) ↔ (0,1) 👉 Undoing your work 😬
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


#  Taking input
n = int(input("Enter size of matrix: "))

matrix = []
print("Enter matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

#  Rotate
rotate(matrix)

#  Output
print("Rotated Matrix:")
for row in matrix:
    print(*row)