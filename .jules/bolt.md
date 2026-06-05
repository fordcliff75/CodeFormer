## 2024-05-19 - NumPy Advanced Indexing for Color Mapping
**Learning:** Using an iterative python loop and boolean masking (`parse_mask[out == idx] = color`) to map class indices to colors creates a new boolean array for every class, resulting in O(N_classes * Image_Size) complexity and huge overhead.
**Action:** Replace these loops with NumPy advanced indexing (`np.array(COLORMAP)[out]`), dropping complexity to O(Image_Size) and providing massive (~30x) speedups for parse mask generation while remaining clean and readable.
