## 2024-08-01 - Replace Python Loops Over Large Numpy Arrays With C-Level Indexing
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., using mask_array[out] instead of out == idx loops) to dramatically improve throughput and prevent type issues.
