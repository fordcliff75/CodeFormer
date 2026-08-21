## YYYY-MM-DD - [Optimize Parsing Mask Creation]
**Learning:** In PyTorch/NumPy computer vision pipelines, iterating element-wise over large boolean arrays in pure Python (like `parse_mask[out == idx] = color` for all classes on a 512x512 array) causes massive CPU bottlenecks (reducing inference speed by >1s per 100 loops).
**Action:** Always replace O(N_classes * Image_Size) boolean mask assignment loops with O(Image_Size) advanced NumPy array indexing (e.g., `np.array(COLORMAP)[out]`) for instantaneous mapping.
