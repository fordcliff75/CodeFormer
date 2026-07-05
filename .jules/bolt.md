## 2025-03-01 - [NumPy Advanced Indexing Optimization]
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace iterative element-wise checking with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput and reduce time complexity from O(N_classes * Image_Size) to O(Image_Size).
