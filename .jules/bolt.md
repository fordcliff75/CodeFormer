## 2024-05-18 - [Optimize Face Parsing Colormap]
**Learning:** An iterative loop mapping face parsing indices to a colormap runs O(N_classes * Image_Size) and creates a bottleneck.
**Action:** Replace `parse_mask[out == idx] = color` loop with NumPy advanced indexing `np.array(MASK_COLORMAP, dtype=float)[out]` to run in O(Image_Size), yielding ~30x speedup.
