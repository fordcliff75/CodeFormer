## 2025-03-08 - Fast Face Parse Map Colormap Application
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g. `parse_mask[out == idx] = color` for 512x512 images) introduce significant CPU bottlenecks when post-processing face masks.
**Action:** Replace iterative mapping over classes with C-level NumPy advanced indexing (`parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) to dramatically improve throughput and prevent data type issues during division later on.
