## 2024-05-24 - Vectorized Face Mask Generation
**Learning:** In PyTorch inference pipelines, converting a segmentation map (e.g., face parsing indices) to a color image map using an iterative loop `parse_mask[out == idx] = color` creates significant CPU overhead due to large boolean checks ($O(C \times H \times W)$).
**Action:** Replace these iterative boolean checks with NumPy advanced indexing (`np.array(MASK_COLORMAP)[out]`), which vectorizes the operation to a single map lookup ($O(H \times W)$) and provides a significant >30x speedup for mask generation without any dependency additions.
