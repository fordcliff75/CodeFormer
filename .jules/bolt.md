## 2024-05-18 - Avoid np.linalg.norm in tight loops for distance calculation
**Learning:** In Python, computing Euclidean distances inside loops by instantiating NumPy arrays and calling `np.linalg.norm()` is incredibly slow due to the overhead of object creation and function calls for small vectors.
**Action:** Replace `np.linalg.norm()` with pure-Python squared distance calculation (e.g. `(x1-x2)**2 + (y1-y2)**2`) inside a list comprehension. This avoids overhead and works perfectly for finding minimum distances (as min(x) == min(x^2) for positive numbers), yielding ~10x speedups in tasks like finding center faces.

## 2024-05-18 - Optimize nested bounds checking
**Learning:** Re-implementing a simple local function for value bounding inside a loop (like `get_location` in `get_largest_face`) creates significant function call overhead in Python.
**Action:** Inline simple bounds checking (e.g., using `if-else` or inline ternary operators) within the loop. Furthermore, finding the largest item in a single pass while calculating its property is much faster than computing all properties into a list and then calling `max()` and `.index()`.
