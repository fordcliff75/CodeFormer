## 2024-06-29 - [Performance Optimization] Optimize face mask colormap mapping
**Learning:** Using an iterative loop to map mask parsing indices to a colormap introduces a CPU bottleneck. Replacing it with NumPy advanced indexing (`parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) reduces time complexity from O(N_classes * Image_Size) to O(Image_Size).
**Action:** Avoid iterative colormap masking loops in the future and always use NumPy advanced indexing for large array replacements.
