import numpy as np

# ==========================================
# 1. Array Creation & Properties
# ==========================================
print("=== 1. Array Creation & Properties ===")
arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr1)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)
print("Dimensions:", arr1.ndim)

# ==========================================
# 2. Arithmetic Operations
# ==========================================
print("\n=== 2. Arithmetic Operations ===")
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# ==========================================
# 3. Aggregation Operations
# ==========================================
print("\n=== 3. Aggregation Operations ===")
arr3 = np.array([12, 45, 67, 89, 23, 56, 78, 90, 34, 11])
print("Maximum:", np.max(arr3))
print("Minimum:", np.min(arr3))
print("Sum:", np.sum(arr3))
print("Average:", np.mean(arr3))

# ==========================================
# 4. Boolean Indexing (Even & Odd)
# ==========================================
print("\n=== 4. Boolean Indexing (Even & Odd) ===")
arr4 = np.arange(1, 21)
even_nums = arr4[arr4 % 2 == 0]
odd_nums = arr4[arr4 % 2 != 0]
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)

# ==========================================
# 5. Reshaping Arrays
# ==========================================
print("\n=== 5. Reshaping Arrays ===")
arr5 = np.arange(1, 13)
print("2 x 6 Matrix:\n", arr5.reshape(2, 6))
print("3 x 4 Matrix:\n", arr5.reshape(3, 4))
print("4 x 3 Matrix:\n", arr5.reshape(4, 3))

# ==========================================
# 6. Matrix Addition
# ==========================================
print("\n=== 6. Matrix Addition ===")
mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix Addition:\n", mat1 + mat2)

# ==========================================
# 7. Matrix Multiplication
# ==========================================
print("\n=== 7. Matrix Multiplication ===")
mat_a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
mat_b = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
print("Matrix Multiplication (matmul):\n", np.matmul(mat_a, mat_b))

# ==========================================
# 8. Matrix Transpose
# ==========================================
print("\n=== 8. Matrix Transpose ===")
mat_3x4 = np.arange(1, 13).reshape(3, 4)
print("Original 3x4 Matrix:\n", mat_3x4)
print("Transpose (4x3):\n", mat_3x4.T)

# ==========================================
# 9. Array Slicing (4x4 Matrix)
# ==========================================
print("\n=== 9. Array Slicing (4x4 Matrix) ===")
mat_4x4 = np.arange(1, 17).reshape(4, 4)
print("4x4 Matrix:\n", mat_4x4)
print("First Row:", mat_4x4[0, :])
print("Last Column:", mat_4x4[:, -1])
print("Diagonal Elements:", np.diagonal(mat_4x4))
print("Second and Third Rows:\n", mat_4x4[1:3, :])

# ==========================================
# 10. Row & Column Sums
# ==========================================
print("\n=== 10. Row & Column Sums ===")
mat_sum = np.arange(1, 17).reshape(4, 4)
print("Row Sums:", np.sum(mat_sum, axis=1))
print("Column Sums:", np.sum(mat_sum, axis=0))

# ==========================================
# 11. Array Slicing Operations
# ==========================================
print("\n=== 11. Array Slicing Operations ===")
arr11 = np.arange(1, 21)
print("First 5 elements:", arr11[:5])
print("Last 5 elements:", arr11[-5:])
print("Alternate elements:", arr11[::2])
print("Elements in reverse order:", arr11[::-1])

# ==========================================
# 12. Replacing Elements > 50
# ==========================================
print("\n=== 12. Replacing Elements > 50 ===")
arr12 = np.array([20, 55, 30, 80, 45, 90, 10, 60, 25, 75])
print("Original Array:", arr12)
arr12[arr12 > 50] = 0
print("Modified Array:", arr12)

# ==========================================
# 13. Sorting (Ascending & Descending)
# ==========================================
print("\n=== 13. Sorting ===")
unsorted_arr = np.array([42, 12, 88, 23, 65, 7, 34])
print("Ascending Order:", np.sort(unsorted_arr))
print("Descending Order:", np.sort(unsorted_arr)[::-1])

# ==========================================
# 14. Unique Elements
# ==========================================
print("\n=== 14. Unique Elements ===")
dup_arr = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6, 6])
print("Unique Elements:", np.unique(dup_arr))

# ==========================================
# 15. Concatenation (Horizontal & Vertical)
# ==========================================
print("\n=== 15. Concatenation ===")
arr15_a = np.array([[1, 2], [3, 4]])
arr15_b = np.array([[5, 6], [7, 8]])
print("Horizontal Concatenation:\n", np.hstack((arr15_a, arr15_b)))
print("Vertical Concatenation:\n", np.vstack((arr15_a, arr15_b)))

# ==========================================
# 16. Marks Statistics (10 Students)
# ==========================================
print("\n=== 16. Marks Statistics (10 Students) ===")
marks_10 = np.array([78, 85, 92, 60, 74, 88, 95, 67, 82, 90])
print("Highest Marks:", np.max(marks_10))
print("Lowest Marks:", np.min(marks_10))
print("Average Marks:", np.mean(marks_10))
print("Median:", np.median(marks_10))
print("Standard Deviation:", np.std(marks_10))

# ==========================================
# 17. Marks Statistics (20 Students - Above Average)
# ==========================================
print("\n=== 17. Marks Statistics (20 Students) ===")
marks_20 = np.array(
    [55, 62, 78, 85, 90, 45, 88, 92, 70, 68, 81, 74, 95, 50, 83, 76, 89, 64, 91, 73]
)
class_avg = np.mean(marks_20)
print(f"Class Average: {class_avg:.2f}")
print("Marks above average:", marks_20[marks_20 > class_avg])

# ==========================================
# 18. 3D Array Creation & Properties
# ==========================================
print("\n=== 18. 3D Array Creation & Properties ===")
arr_3d_18 = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr_3d_18)
print("Number of Dimensions:", arr_3d_18.ndim)
print("Shape:", arr_3d_18.shape)
print("Size:", arr_3d_18.size)

# ==========================================
# 19. 3D Array Indexing
# ==========================================
print("\n=== 19. 3D Array Indexing ===")
arr_3d_19 = np.arange(1, 25).reshape(2, 3, 4)
print("First Element:", arr_3d_19[0, 0, 0])
print("Last Element:", arr_3d_19[-1, -1, -1])
print("Element at index [0, 1, 2]:", arr_3d_19[0, 1, 2])
print("Element at index [1, 2, 3]:", arr_3d_19[1, 2, 3])

# ==========================================
# 20. 3D Array Sums
# ==========================================
print("\n=== 20. 3D Array Sums ===")
arr_3d_20 = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of all elements:", np.sum(arr_3d_20))
print("Sum of each layer (axis=(1,2)):", np.sum(arr_3d_20, axis=(1, 2)))
print("Sum along rows (axis=1):\n", np.sum(arr_3d_20, axis=1))
print("Sum along columns (axis=2):\n", np.sum(arr_3d_20, axis=2))

# ==========================================
# 21. Random 3D Array Modification
# ==========================================
print("\n=== 21. Random 3D Array Modification ===")
np.random.seed(42)  # For reproducible random output
rand_3d_21 = np.random.randint(1, 101, size=(2, 3, 4))
print("Original Random 3D Array:\n", rand_3d_21)
rand_3d_21[rand_3d_21 > 50] = 0
print("\nModified Array (values > 50 set to 0):\n", rand_3d_21)

# ==========================================
# 22. Random 3D Array Statistics (3, 4, 5)
# ==========================================
print("\n=== 22. Random 3D Array Statistics ===")
rand_3d_22 = np.random.randint(1, 101, size=(3, 4, 5))
print("Mean:", np.mean(rand_3d_22))
print("Median:", np.median(rand_3d_22))
print("Standard Deviation:", np.std(rand_3d_22))
print("Variance:", np.var(rand_3d_22))
print("Minimum:", np.min(rand_3d_22))
print("Maximum:", np.max(rand_3d_22))

# ==========================================
# 23. Flattening 3D Array
# ==========================================
print("\n=== 23. Flattening 3D Array ===")
arr_3d_23 = np.arange(1, 25).reshape(2, 3, 4)
flattened_23 = arr_3d_23.flatten()
print("Original 3D Array:\n", arr_3d_23)
print("Flattened Array:\n", flattened_23)

# ==========================================
# 24. Flattened 3D Array Operations (1 to 27)
# ==========================================
print("\n=== 24. Flattened 3D Array Operations ===")
arr_3d_24 = np.arange(1, 28).reshape(3, 3, 3)
flattened_24 = arr_3d_24.flatten()
print("Sum:", np.sum(flattened_24))
print("Average:", np.mean(flattened_24))
print("Maximum:", np.max(flattened_24))
print("Minimum:", np.min(flattened_24))

# ==========================================
# 25. Filtering Flattened 3D Random Array
# ==========================================
print("\n=== 25. Filtering Flattened 3D Random Array ===")
rand_3d_25 = np.random.randint(1, 101, size=(3, 4, 5))
flattened_25 = rand_3d_25.flatten()
avg_val_25 = np.mean(flattened_25)

print("Flattened Array:\n", flattened_25)
print("\nElements > 50:", flattened_25[flattened_25 > 50])
print("Even elements:", flattened_25[flattened_25 % 2 == 0])
print(
    f"Elements < Average ({avg_val_25:.2f}):",
    flattened_25[flattened_25 < avg_val_25],
)