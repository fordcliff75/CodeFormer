## YYYY-MM-DD - Performance Bottleneck in Mask Creation
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks during model inference.
**Action:** Replace iterative loops mapping face parsing indices to a colormap with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to dramatically improve throughput.
