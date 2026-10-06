# =============================================================================
# DAY 29: DATA ANALYSIS & NUMPY (BASIC LEVEL)
# Author: Harish
# Repository: DAY-29-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

import numpy as np

# =============================================================================
# 1. CREATING NUMPY ARRAYS
# =============================================================================
print("--- 1. CREATING ARRAYS ---")

# 1D Array (Vector)
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# 2D Array (Matrix)
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D Array:\n", arr2)


# =============================================================================
# 2. ARRAY ATTRIBUTES
# =============================================================================
print("\n--- 2. ARRAY ATTRIBUTES ---")

print("Dimensions (ndim) :", arr2.ndim)
print("Shape (rows, cols):", arr2.shape)
print("Total elements    :", arr2.size)
print("Data type         :", arr2.dtype)


# =============================================================================
# 3. BUILT-IN ARRAY CREATION FUNCTIONS
# =============================================================================
print("\n--- 3. BUILT-IN ARRAY FUNCTIONS ---")

# Array of all zeros
zeros = np.zeros((2, 3))
print("Zeros (2x3):\n", zeros)

# Array of all ones
ones = np.ones((2, 2))
print("\nOnes (2x2):\n", ones)

# Array with a range of numbers (start, stop, step)
range_arr = np.arange(1, 10, 2)
print("\nNumbers from 1 to 10 with step 2:", range_arr)


# =============================================================================
# 4. INDEXING AND SLICING
# =============================================================================
print("\n--- 4. INDEXING AND SLICING ---")

nums = np.array([10, 20, 30, 40, 50])
print("Original Array:", nums)
print("First element :", nums[0])
print("Last element  :", nums[-1])
print("Slice [1:4]   :", nums[1:4])

# 2D Slicing: [row, column]
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("\nMatrix:\n", matrix)
print("Element at row 0, col 1 :", matrix[0, 1])
print("Entire first row        :", matrix[0, :])
print("Entire second column    :", matrix[:, 1])


# =============================================================================
# 5. BASIC ARITHMETIC OPERATIONS (VECTORIZATION)
# =============================================================================
print("\n--- 5. BASIC ARITHMETIC OPERATIONS ---")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("a + b :", a + b)
print("a - b :", a - b)
print("a * b :", a * b)
print("a / b :", a / b)
print("a * 2 :", a * 2)  # Scalar multiplication


# =============================================================================
# 6. BASIC DATA ANALYSIS & STATISTICAL FUNCTIONS
# =============================================================================
print("\n--- 6. DATA ANALYSIS FUNCTIONS ---")

scores = np.array([65, 78, 82, 90, 95])
print("Scores:", scores)

print("Total Sum :", np.sum(scores))
print("Average   :", np.mean(scores))
print("Minimum   :", np.min(scores))
print("Maximum   :", np.max(scores))


# =============================================================================
# 7. FILTERING DATA (CONDITIONS)
# =============================================================================
print("\n--- 7. FILTERING DATA ---")

marks = np.array([45, 60, 30, 85, 92, 28])
print("All marks:", marks)

# Filter marks greater than or equal to 50 (Pass marks)
pass_marks = marks[marks >= 50]
print("Passing marks (>= 50):", pass_marks)
