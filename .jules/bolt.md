
## 2024-05-30 - [Optimize Colormap Assignment in face_restoration_helper.py]
**Learning:** Using an iterative python loop to assign colormaps to segmentation masks is an $O(N\_classes \times Image\_Size)$ operation that scales poorly with image size or number of classes.
**Action:** Replace boolean assignment loops mapping classes to colors with idiomatic NumPy advanced indexing: `parse_mask = np.array(MASK_COLORMAP)[out]`. This leverages underlying C code to assign classes in $O(Image\_Size)$ time and significantly reduces execution time.
