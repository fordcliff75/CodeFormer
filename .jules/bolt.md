## 2024-05-24 - Efficient finding max/min elements in Python
**Learning:** Finding the max element of derived values (e.g., face bounding box area or face center distance) is significantly faster with a single-pass tracking loop instead of list comprehension + max(list) + list.index().
**Action:** Use a single-pass for loop when computing properties to find a min/max, avoiding intermediate list allocation overhead.
