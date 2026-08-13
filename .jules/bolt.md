## 2024-08-13 - Optimize face parsing mask creation
**Learning:** During model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput.
