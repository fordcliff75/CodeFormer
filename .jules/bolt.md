## 2024-05-15 - Numpy advanced indexing for colormap mapping
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., face segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput.
