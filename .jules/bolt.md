## 2024-05-24 - Optimization of face parsing mask loop
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks during model inference.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., using `mask_array[out]`) to dramatically improve throughput.
