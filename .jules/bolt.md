
## 2024-05-28 - [Performance] Vectorize PyTorch/NumPy Index Mapping
**Learning:** An iterative loop mapping a list of colormaps onto an index mask (`out == idx`) takes O(N_classes * H * W). When processing `512x512` images with 19 classes, this slow pure-Python loop severely bottlenecks frame processing.
**Action:** When mapping discrete integer index tensors (e.g. segmentation outputs) to colors, always use NumPy advanced/vectorized indexing like `np.array(COLORMAP)[index_tensor]` to shift the operation to C and achieve O(H * W) time complexity.
