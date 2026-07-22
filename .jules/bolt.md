## 2025-02-23 - [Optimize face mask colormap mapping]
**Learning:** Replaced an iterative boolean masking loop (`parse_mask[out == idx] = color`) with NumPy advanced indexing (`np.array(MASK_COLORMAP)[out]`). This prevents creating multiple large boolean arrays (512x512) and iterating repeatedly in Python during model inference post-processing.
**Action:** Always look for opportunities to replace element-wise Python loops over large NumPy arrays with C-level advanced indexing or vectorized operations to eliminate significant CPU bottlenecks during inference.
