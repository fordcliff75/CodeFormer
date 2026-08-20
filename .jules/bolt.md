## 2025-02-20 - NumPy Advanced Indexing Over Iterative Mask Loops
**Learning:** During image processing inferences (e.g., in CodeFormer face parsing), using iterative Python loops with boolean checking (`parse_mask[out == idx] = color`) to apply a colormap to a segmentation map is a substantial CPU bottleneck.
**Action:** Always replace O(N_classes * Image_Size) iterative boolean mask mappings with O(Image_Size) C-level NumPy advanced indexing (`np.array(MASK_COLORMAP)[out]`) to optimize array constructions in deep learning data processing pipelines.
