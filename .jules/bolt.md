## 2025-02-12 - [NumPy Advanced Indexing Optimization]
**Learning:** Iterative Python boolean masking loops for large segmentation maps (e.g. 512x512) introduce significant CPU bottlenecks.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., using `mask_array[out]`) to dramatically improve throughput and prevent type issues.
