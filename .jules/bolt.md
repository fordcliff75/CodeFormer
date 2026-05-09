## 2024-05-24 - [Optimize np.linalg.norm with Pure Python Squared Distance]
**Learning:** Using `np.linalg.norm` and instantiating NumPy arrays inside loops for basic point-distance calculations introduces significant overhead (~5.5x slower) compared to calculating raw squared Euclidean distance `(dx**2 + dy**2)` directly in Python, while achieving the exact same monotonic result for `min()` logic.
**Action:** Replace `np.linalg.norm()` and temporary `np.array` allocations inside tight point-distance loops with pure Python squared difference logic to massively reduce iteration overhead.
