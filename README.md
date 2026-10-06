# Day 29: Data Analysis & NumPy in Python 📊🔢🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-29-OF-PYTHON](https://github.com/harish-0987/DAY-29-OF-PYTHON)

Welcome to **Day 29 of Python**! Today's session explores **Data Analysis & NumPy in Python**—the foundational, industry-standard cornerstone of modern scientific computing, data science, and machine learning—explained from basic-level principles with clear mental models, practical code examples, and a real-world analytics pipeline.

> [!NOTE]
> **Scope for Today**: We cover what Data Analysis is, why NumPy is preferred over native Python lists, array creation (`np.array`, `arange`, `linspace`), key attributes (`ndim`, `shape`, `size`, `dtype`, `nbytes`), special initializers (`zeros`, `ones`, `eye`, `random`), multidimensional indexing & slicing, vectorized operations, broadcasting mechanics, statistical reductions (`mean`, `median`, `std`, `min`, `max`, `argmax`, axis=0 vs axis=1), boolean masking & `np.where()`, matrix reshaping & transposing, and a real-world **E-Commerce Retail Store Sales & Revenue Analytics Engine**.

---

## 📌 Table of Contents

1. [What is Data Analysis & NumPy? (Basic Level)](#-what-is-data-analysis--numpy-basic-level)
2. [Real-World Analogies](#-real-world-analogies)
3. [Why NumPy Over Standard Python Lists?](#-why-numpy-over-standard-python-lists)
4. [NumPy Architecture: Contiguous Memory & Vectorization](#-numpy-architecture-contiguous-memory--vectorization)
5. [Core Features & Code Demonstrations](#-core-features--code-demonstrations)
   - [1. Array Creation & Data Types](#1-array-creation--data-types)
   - [2. Essential Array Attributes](#2-essential-array-attributes)
   - [3. Special Array Initializers & Random Numbers](#3-special-array-initializers--random-numbers)
   - [4. Multidimensional Indexing & Slicing](#4-multidimensional-indexing--slicing)
   - [5. Vectorization vs. Python Loops (Performance Benchmark)](#5-vectorization-vs-python-loops-performance-benchmark)
   - [6. Broadcasting Mechanics](#6-broadcasting-mechanics)
   - [7. Statistical & Mathematical Reductions (Axis 0 vs Axis 1)](#7-statistical--mathematical-reductions-axis-0-vs-axis-1)
   - [8. Filtering, Boolean Masking & `np.where()`](#8-filtering-boolean-masking--npwhere)
   - [9. Array Reshaping, Transposing & Flattening](#9-array-reshaping-transposing--flattening)
   - [10. Array Stacking & Splitting](#10-array-stacking--splitting)
6. [Real-World Case Study: Retail Sales Analytics Engine](#-real-world-case-study-retail-sales-analytics-engine)
7. [NumPy Data Analysis Cheat Sheet Matrix](#-numpy-data-analysis-cheat-sheet-matrix)
8. [How to Run the Code](#-how-to-run-the-code)

---

## 💡 What is Data Analysis & NumPy? (Basic Level)

**Data Analysis** is the science and art of inspecting, cleaning, transforming, and modeling raw numerical and categorical information to discover patterns, draw conclusions, and make informed decisions.

**NumPy** (*Numerical Python*) is the core library in Python designed specifically for high-performance numerical and scientific computing. It introduces the **`ndarray`** (N-dimensional array), a fast, memory-efficient data structure for storing collections of homogeneous numbers.

```
       ┌────────────────────────────────────────────────────────┐
       │                   PYTHON LIST                          │
       │  [ Pointer ] ──> [ PyObject: Integer 10 ]               │
       │  [ Pointer ] ──> [ PyObject: String "hello" ]          │ (Scattered RAM, slow)
       │  [ Pointer ] ──> [ PyObject: Float 3.14 ]              │
       └────────────────────────────────────────────────────────┘

       ┌────────────────────────────────────────────────────────┐
       │                   NUMPY NDARRAY                        │
       │  ┌───────┬───────┬───────┬───────┬───────┬───────┐      │
       │  │  10   │  20   │  30   │  40   │  50   │  60   │      │ (Contiguous C block,
       │  └───────┴───────┴───────┴───────┴───────┴───────┘      │  lightning fast!)
       └────────────────────────────────────────────────────────┘
```

---

## 🚗 Real-World Analogies

1. **The Automated Assembly Line vs. One-By-One Handcrafting**:
   - In a standard Python loop, an interpreter processes each list item one by one, inspecting its type, unboxing it, and computing the result.
   - NumPy functions like an automated factory press: it performs an identical mathematical operation across millions of elements in a single synchronized stroke (**Vectorization**).

2. **The Multi-Dimensional Spreadsheet**:
   - **1D Array (Vector)** = A single column or row of numbers (e.g., student marks).
   - **2D Array (Matrix)** = A complete grid table with rows and columns (e.g., monthly sales figures for multiple store branches).
   - **3D Array (Tensor)** = A stack of spreadsheets representing multiple years or geographic regions.

3. **Digital Photography & Image Pixels**:
   - Every photograph on your smartphone or camera is fundamentally stored as a NumPy array:
     - Grayscale image: 2D array of brightness values `[Height, Width]`.
     - Color photo: 3D array `[Height, Width, 3]` (Red, Green, Blue channels).
   - When you adjust brightness or contrast, image processing software multiplies or adds constants across the entire NumPy matrix simultaneously!

---

## ⚡ Why NumPy Over Standard Python Lists?

| Dimension | Python Built-In List | NumPy `ndarray` |
| :--- | :--- | :--- |
| **Data Types** | Heterogeneous (can mix strings, ints, floats) | Homogeneous (all elements have the exact same type) |
| **Memory Storage** | Scattered pointers to independent Python objects | Contiguous contiguous memory blocks in RAM |
| **Computation Speed** | Slow interpreted loops in Python bytecode | Compiled C/Fortran vector routines (10x – 50x faster) |
| **Mathematical Operations** | Does not support element-wise math (`+` concatenates) | Full support for vector math (`arr * 2`, `arr1 + arr2`) |
| **Multidimensionality** | Nested lists (`[[1, 2], [3, 4]]`) with awkward slicing | Native N-dimensional indexing, slicing, and reshaping |
| **Ecosystem Role** | General programming | Foundation of Pandas, Scikit-learn, PyTorch, SciPy |

---

## ⚙️ Core Features & Code Demonstrations

### 1. Array Creation & Data Types

NumPy allows creating arrays from lists or via built-in generators:

```python
import numpy as np

# 1D Array (Vector)
arr_1d = np.array([10, 20, 30, 40, 50])

# 2D Array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Evenly spaced numbers with a step (start, stop, step)
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Evenly spaced numbers with fixed point count (start, stop, num)
linear_points = np.linspace(0.0, 1.0, 5)  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

### 2. Essential Array Attributes

Inspect the dimensions, size, and RAM consumption of an array:

```python
matrix = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.int32)

print(matrix.ndim)      # 2 (Number of dimensions / axes)
print(matrix.shape)     # (2, 3) -> 2 rows, 3 columns
print(matrix.size)      # 6 (Total element count)
print(matrix.dtype)     # int32 (Data type)
print(matrix.itemsize)  # 4 bytes per integer
print(matrix.nbytes)    # 24 bytes total memory footprint
```

### 3. Special Array Initializers & Random Numbers

```python
# Matrix of zeros or ones
zeros = np.zeros((3, 4))   # 3 rows x 4 columns of 0.0
ones = np.ones((2, 3))     # 2 rows x 3 columns of 1.0

# Constant fill matrix
sevens = np.full((2, 2), 7)

# Identity Matrix (1s on diagonal, 0s elsewhere)
eye_matrix = np.eye(3)

# Reproducible random numbers
np.random.seed(42)
random_floats = np.random.rand(2, 3)              # Uniform [0, 1)
random_integers = np.random.randint(10, 100, (3, 3)) # Integers [10, 100)
```

### 4. Multidimensional Indexing & Slicing

Extract specific elements, complete rows, columns, or sub-matrices using `arr[row_slice, col_slice]`:

```python
grid = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# Specific cell (Row 1, Column 2)
print(grid[1, 2])       # Output: 70

# Complete Row 0
print(grid[0, :])       # Output: [10, 20, 30, 40]

# Complete Column 1
print(grid[:, 1])       # Output: [20, 60, 100]

# Sub-matrix (Rows 0 to 1, Columns 1 to 2)
print(grid[0:2, 1:3])
# [[20, 30],
#  [60, 70]]
```

### 5. Vectorization vs. Python Loops (Performance Benchmark)

NumPy eliminates the need for slow Python `for` loops by executing element-wise operations directly at compiled C speed:

```python
prices = np.array([100.0, 250.0, 499.0, 1200.0])
discount = 0.10  # 10% discount
tax = 0.18       # 18% GST

# Applied to ALL elements simultaneously in a single vectorized statement
final_prices = (prices * (1 - discount)) * (1 + tax)
# Output: [106.2, 265.5, 529.94, 1274.4]
```

> 🚀 **Benchmark Fact**: When adding two 1,000,000-element arrays, NumPy is typically **15x to 50x faster** than a pure Python list comprehension.

### 6. Broadcasting Mechanics

Broadcasting allows arithmetic operations between arrays of different shapes without copying data:

```
Exam Scores (4x3):             Curve (3,):              Result (4x3):
┌────┬────┬────┐               ┌───┬───┬───┐            ┌────┬────┬────┐
│ 70 │ 80 │ 85 │               │ 5 │ 2 │ 0 │            │ 75 │ 82 │ 85 │
├────┼────┼────┤   Broadcast   └───┴───┴───┘            ├────┼────┼────┤
│ 65 │ 75 │ 90 │   ─────────>                           │ 70 │ 77 │ 90 │
├────┼────┼────┤   (Row-wise)  Duplicates automatically ├────┼────┼────┤
│ 90 │ 95 │ 92 │               across all 4 rows        │ 95 │ 97 │ 92 │
├────┼────┼────┤                                        ├────┼────┼────┤
│ 60 │ 62 │ 70 │                                        │ 65 │ 64 │ 70 │
└────┴────┴────┘                                        └────┴────┴────┘
```

```python
exam_scores = np.array([
    [70, 80, 85],
    [65, 75, 90],
    [90, 95, 92],
    [60, 62, 70]
])
curve = np.array([5, 2, 0])

curved_scores = exam_scores + curve  # Automatically broadcasts!
```

### 7. Statistical & Mathematical Reductions (Axis 0 vs Axis 1)

In data analysis:
- **`axis=0`**: Aggregates down the **columns** (collapsing rows into one summary row).
- **`axis=1`**: Aggregates across the **rows** (collapsing columns into one summary column).

```python
sales = np.array([
    [15, 22, 19],  # Rep 1
    [30, 28, 35],  # Rep 2
    [12, 14, 11]   # Rep 3
])

print(np.sum(sales))            # Global total: 186
print(np.mean(sales))           # Global average: 20.67
print(np.sum(sales, axis=0))    # Column totals: [57, 64, 65]
print(np.sum(sales, axis=1))    # Row totals:    [56, 93, 37]
print(np.argmax(np.sum(sales, axis=1)))  # Index of highest sales rep (1 -> Rep 2)
```

### 8. Filtering, Boolean Masking & `np.where()`

```python
temperatures = np.array([28.5, 32.0, 41.2, 19.8, 38.6, 43.1])

# 1. Boolean mask
is_hot = temperatures >= 35.0   # [False, False, True, False, True, True]

# 2. Filter elements
hot_days = temperatures[is_hot] # [41.2, 38.6, 43.1]

# 3. Compound condition (& = AND, | = OR, ~ = NOT)
pleasant = temperatures[(temperatures >= 20.0) & (temperatures < 35.0)]

# 4. Vectorized ternary (if-else condition)
labels = np.where(temperatures >= 40.0, "HEAT_WAVE", "NORMAL")
```

### 9. Array Reshaping, Transposing & Flattening

```python
arr = np.arange(1, 13)         # 1D array of 12 numbers

# Reshape to 3 rows x 4 columns
matrix = arr.reshape((3, 4))

# Automatic dimension deduction with -1
matrix_2x6 = arr.reshape((2, -1))

# Transpose (swap rows and columns)
transposed = matrix.T          # Shape becomes (4, 3)

# Flatten back to 1D
flat = matrix.flatten()
```

### 10. Array Stacking & Splitting

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stack vertically (adds rows)
v = np.vstack((a, b))  # Shape (4, 2)

# Stack horizontally (joins columns)
h = np.hstack((a, b))  # Shape (2, 4)

# Split into equal pieces
chunks = np.split(np.arange(6), 3)  # [[0, 1], [2, 3], [4, 5]]
```

---

## 📊 Real-World Case Study: Retail Sales Analytics Engine

The module includes an executable class `RetailAnalyticsEngine` demonstrating how to build an end-to-end sales analytics pipeline for an online retail store tracking 5 products over 7 days:

```
──────────────────────────────────────────────────────────────────────
  📊 E-COMMERCE WEEKLY SALES & REVENUE EXECUTIVE REPORT
──────────────────────────────────────────────────────────────────────
Product          | Unit Price | Units Sold | Revenue (INR) 
───────────────────────────────────────────────────────────
Wireless Mouse   | ₹  499.00 |        205 | ₹  102,295.00
Mechanical KB    | ₹ 2499.00 |         76 | ₹  189,924.00
USB-C Hub        | ₹  899.00 |        101 | ₹   90,799.00
27' Monitor      | ₹14999.00 |         36 | ₹  539,964.00
HD Webcam        | ₹ 1899.00 |         66 | ₹  125,334.00
───────────────────────────────────────────────────────────
TOTAL GROSS REVENUE : ₹1,048,316.00
AVERAGE DAILY REVENUE: ₹149,759.43
🏆 BEST-SELLING ITEM : Wireless Mouse (Highest volume)
💰 TOP REVENUE ITEM  : 27' Monitor (Highest earnings)
📅 PEAK SALES DAY    : Sun
──────────────────────────────────────────────────────────────────────
```

---

## 📋 NumPy Data Analysis Cheat Sheet Matrix

| Category | Method / Syntax | Description & Purpose |
| :--- | :--- | :--- |
| **Array Creation** | `np.array(iterable)` | Converts list / tuple to ndarray with homogeneous dtype. |
| | `np.arange(start, stop, step)` | Generates array with evenly spaced step intervals. |
| | `np.linspace(start, stop, n)` | Generates n evenly distributed numbers across an interval. |
| | `np.zeros(shape)` / `np.ones()` | Initializes array populated entirely with 0s or 1s. |
| | `np.full(shape, val)` / `np.eye(n)`| Initializes with constant value or creates Identity Matrix. |
| **Attributes** | `.ndim`, `.shape`, `.size` | Number of dimensions, tuple of axes sizes, total elements. |
| | `.dtype`, `.nbytes` | Element data type, total RAM consumption in bytes. |
| **Indexing & Slicing** | `arr[i, j]` | Selects element at row i, column j. |
| | `arr[r1:r2, c1:c2]` | Extracts sub-matrix across row and column ranges. |
| | `arr[:, k]` / `arr[k, :]` | Extracts entire column k or entire row k. |
| **Vectorized Math** | `arr1 + arr2`, `arr * scalar` | Element-wise arithmetic without Python for-loops. |
| | **Broadcasting** | Automatic dimension expansion for compatible shapes. |
| **Statistical Metrics**| `np.sum()`, `np.mean()` | Aggregates sum, arithmetic mean across array or axis. |
| | `np.median()`, `np.std()` | Computes median and standard deviation. |
| | `np.min()`, `np.max()` | Finds minimum and maximum values. |
| | `np.argmin()`, `np.argmax()` | Returns index of minimum or maximum value. |
| **Filtering & Masking**| `arr[arr > threshold]` | Boolean masking: extracts elements satisfying condition. |
| | `np.where(cond, x, y)` | Vectorized if-else: returns x where True, y where False. |
| **Reshaping** | `arr.reshape((r, c))` | Reconfigures array geometry (total size must match). |
| | `arr.T` | Transposes matrix (swaps rows and columns). |
| | `arr.flatten()` / `arr.ravel()` | Flattens multidimensional array to 1D vector. |
| **Stacking & Splitting**| `np.vstack()`, `np.hstack()` | Vertically stacks rows or horizontally joins columns. |
| | `np.split(arr, sections)` | Divides array into equal sub-array chunks. |

---

## 🚀 How to Run the Code

1. Ensure Python 3.8+ and NumPy are installed:
   ```bash
   pip install numpy
   ```

2. Run the Day 29 script directly:
   ```bash
   python day29.py
   ```

3. All 12 demonstration sections, performance benchmarks, and the retail case study will execute and display cleanly formatted results in your terminal!

---

> **Day 29 Complete**: Data Analysis & NumPy fundamentals mastered!  
> *"Not here to be known, here to build."*
