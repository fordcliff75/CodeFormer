## 2024-05-13 - [Fast Mask Colormap Generation]
**Learning:** Using iterative loops to map segmentation parsing indices to a colormap introduces a severe CPU bottleneck during inference for high-resolution images.
**Action:** Always utilize NumPy advanced indexing (`np.array(colormap)[indices]`) to map class indices to colors/values efficiently in O(N) time without Python loop overhead.
