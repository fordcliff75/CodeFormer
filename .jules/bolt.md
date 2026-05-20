## 2024-05-20 - [Refactoring Numpy Advanced Indexing for Parsing Mask Colormap]
**Learning:** Using Numpy advanced indexing for colormap mapping (`parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) reduces execution time by over 30x compared to iterating over classes and mapping via `out == idx`.
**Action:** Always prefer advanced indexing over iterative conditionals for mapping discrete labels to continuous or vector variables using a colormap when using NumPy arrays.
