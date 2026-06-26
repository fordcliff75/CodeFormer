## 2026-06-26 - NumPy Advanced Indexing Optimization
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks. Replacing them with C-level NumPy advanced indexing (e.g., using mask_array[out] instead of out == idx loops) dramatically improves throughput.
**Action:** Always favor NumPy advanced indexing and vectorization over explicit loops when mapping values or categories across large arrays.
