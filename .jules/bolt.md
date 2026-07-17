## 2025-01-01 - [NumPy Advanced Indexing for Colormaps]
**Learning:** [In facelib/utils/face_restoration_helper.py, replacing an iterative loop that maps face parsing indices to a colormap with NumPy advanced indexing reduces time complexity from O(N_classes * Image_Size) to O(Image_Size)]
**Action:** [Use NumPy advanced indexing (e.g. `np.array(COLORMAP)[mask]`) instead of mapping masks with iterative for-loops and boolean masking for performance in tight ML pipelines]
