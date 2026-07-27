## 2025-02-12 - [NumPy Advanced Indexing Optimization]
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks. Replacing them with C-level NumPy advanced indexing (e.g., `mask_array[out]` instead of `out == idx` loops) dramatically improves throughput.
**Action:** When mapping indices to values (like a colormap), use NumPy advanced indexing instead of iterative assignment loops.
