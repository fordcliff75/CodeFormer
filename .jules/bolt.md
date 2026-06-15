## 2024-06-15 - Fast colormap indexing with Numpy
**Learning:** In `facelib/utils/face_restoration_helper.py`, an iterative loop maps face parsing indices to a colormap, replacing it with NumPy advanced indexing (`parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) reduces time complexity and CPU bottlenecks.
**Action:** Replace `for` loop mapping colormaps to segmentation masks with `np.array(...)[out]` NumPy advanced indexing to avoid Python iteration over large maps.
