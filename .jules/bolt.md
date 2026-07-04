## 2024-05-24 - NumPy Advanced Indexing for Segmentation Maps
**Learning:** During model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks.
**Action:** Replace iterative boolean masking loops over classes with C-level NumPy advanced indexing (e.g., using `mask_array[out]` instead of `out == idx` loops) to reduce time complexity from O(N_classes * Image_Size) to O(Image_Size) and prevent type issues.
