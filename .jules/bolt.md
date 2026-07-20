## 2024-05-30 - [NumPy Advanced Indexing for Image Masking]
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks during model inference.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput and prevent type issues.
