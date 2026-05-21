## 2024-11-20 - Vectorized colormap mapping in Face Restoration
**Learning:** Using iterative boolean array indexing in a `for` loop to map segmentation classes to RGB colors (`parse_mask[out == idx] = color`) creates a severe O(N_classes * Image_Size) performance bottleneck in `facelib/utils/face_restoration_helper.py`.
**Action:** Always replace this pattern with NumPy advanced indexing (`np.array(COLORMAP)[class_indices]`), which performs the mapping in a single O(Image_Size) operation and yields a >30x speedup in isolated benchmarks without sacrificing readability.
