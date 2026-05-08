
## 2024-05-30 - [Optimize Optimal Face Calculation]
**Learning:** For optimal point distance and area calculation over sets of arrays (like object bounding boxes or face boxes), employing pure-python single-pass loops with inline bounding logic and squared Euclidean distance calculation inside simple list comprehensions avoids creating overhead from repeated small np.array instantiations and expensive `np.linalg.norm` calculations. This improves the tight loops considerably.
**Action:** Always favor inline Python variable checking and pure Python mathematical computation inside a single pass loop or list comprehension compared to instantiating multi-element Numpy Arrays or looping to call helper functions when computing distance and area within tight loops across object lists.
