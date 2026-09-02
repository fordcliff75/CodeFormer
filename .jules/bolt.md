## 2025-02-14 - Python iterative boolean masking bottleneck
**Learning:** Python iterative loops using boolean mask indexing over large spatial arrays (like a 512x512 segmentation map for 19 classes) create massive CPU overhead.
**Action:** Always replace O(N_classes * Image_Size) loop indexing with C-level numpy advanced indexing (array-of-colors mapped by array-of-indices), avoiding redundant O(Image_Size) initialization overhead.
