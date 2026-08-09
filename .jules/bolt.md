## 2024-08-09 - NumPy Advanced Indexing Optimization
**Learning:** During model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace iterative boolean masking loops with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput and prevent type issues.
