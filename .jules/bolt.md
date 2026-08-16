## YYYY-MM-DD - Optimize parsing mask creation with NumPy advanced indexing
**Learning:** During model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks. Replacing them with C-level NumPy advanced indexing (e.g., using mask_array[out] instead of out == idx loops) dramatically improves throughput.
**Action:** Use NumPy advanced indexing instead of iterative loops when mapping indices to values on large arrays.
