## 2026-04-18 - [Avoid np.linalg.norm in pure python loops]
**Learning:** The np.linalg.norm causes large array allocation overhead, pure python squared distance is faster.
**Action:** Use pure Python for euclidean distance inside python loops to avoid memory allocations and speed up processing.
