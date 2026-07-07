## YYYY-MM-DD - [Optimizing Face Mask Parsing]
**Learning:** Iterative loops executing element-wise checking against large numpy arrays in Python introduce significant CPU bottlenecks.
**Action:** Replace with C-level NumPy advanced indexing (e.g., `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput and prevent type issues.
