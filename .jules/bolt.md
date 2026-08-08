## 2024-08-08 - [NumPy Advanced Indexing for Parse Mask]
**Learning:** In `facelib/utils/face_restoration_helper.py`, replacing an iterative loop that maps face parsing indices to a colormap with NumPy advanced indexing (`parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) reduces time complexity from O(N_classes * Image_Size) to O(Image_Size) and prevents type issues during subsequent division operations.
**Action:** Always replace O(N) iterative mask/colormap assignments with NumPy advanced indexing for significant speedups.
