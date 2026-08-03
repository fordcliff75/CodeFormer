## 2024-08-03 - [Numpy Vectorization for Semantic Mapping]
**Learning:** Iterating element-wise mapping in python over large 2D arrays (e.g. segmentation outputs like 512x512) for masking introduces massive CPU bottlenecks.
**Action:** Always prefer C-level NumPy advanced indexing (e.g. `colormap_array[mask]`) instead of mapping elements via O(N_classes * Image_Size) boolean masks.
