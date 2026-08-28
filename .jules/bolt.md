## YYYY-MM-DD - Optimize Parsing Mask Creation
**Learning:** During model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace iterative boolean masking with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput and avoid O(N) operations over color classes.
