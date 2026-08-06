## 2024-08-06 - NumPy advanced indexing for mapping labels
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks in model inference pipelines.
**Action:** Replace iterative O(N_classes * Image_Size) loops with C-level NumPy advanced indexing (e.g., `np.array(COLORMAP)[out]`) to reduce time complexity to O(Image_Size) and dramatically improve throughput.
