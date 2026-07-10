## 2024-06-12 - Face Parsing Advanced Indexing Optimization
**Learning:** Python iteration and element-wise NumPy equality checks (`out == idx`) within tight loops (like face parsing colormap mapping) create severe CPU bottlenecks, scaling poorly with array size and class count `O(N_classes * Image_Size)`.
**Action:** Replace iterative boolean mask construction with C-level NumPy advanced indexing (`np.array(MASK_COLORMAP)[out]`), which vectorizes the operation to `O(Image_Size)`, resulting in ~30x faster mask construction and eliminating the bottleneck.
