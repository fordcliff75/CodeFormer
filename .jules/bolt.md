## 2024-06-20 - [NumPy Advanced Indexing for Segmentation Maps]
**Learning:** Iterative loops executing element-wise checking (`out == idx`) against large NumPy arrays (e.g., 512x512 face segmentation maps) introduce significant CPU bottlenecks during model inference.
**Action:** Replace iterative boolean masking with C-level NumPy advanced indexing (`mask_array[out]`) to map indices to values, which dramatically improves throughput and avoids unnecessary array allocations.
