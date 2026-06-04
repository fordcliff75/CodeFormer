## 2023-10-27 - [NumPy advanced indexing for colormap mapping]
**Learning:** [In a face restoration utility, mapping network inference output classes to colormaps iteratively using a loop (e.g. `parse_mask[out == idx] = color` across 19 classes) is slow, scaling with O(N_classes * Image_Size). A test showed an iterative loop taking ~1.2s, while a vectorized operation taking ~0.04s, yielding ~30x speedup.]
**Action:** [Use NumPy advanced indexing (e.g. `parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) instead of iterative loops for mapping categorical indices to values.]
