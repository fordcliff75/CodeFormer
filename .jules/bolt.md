
## 2024-05-07 - [Vectorized colormap mapping in Face Parse]
**Learning:** In `facelib/utils/face_restoration_helper.py`, mapping face parsing indices to a colormap using an iterative loop (`parse_mask[out == idx] = color` for each class) is highly inefficient.
**Action:** Replace manual iterative loops that map indices to a colormap with NumPy advanced indexing (`parse_mask = np.array(MASK_COLORMAP)[out]`). This reduces time complexity from O(N_classes * Image_Size) to O(Image_Size) and is significantly faster in tight loops.
