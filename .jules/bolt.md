## 2026-02-01 - [Mask Colormap Indexing Optimization]
**Learning:** Python iterative `for` loops combined with boolean masking (e.g. `parse_mask[out == idx] = color`) are extremely slow for pixel color mapping.
**Action:** Always replace them with single-pass NumPy advanced integer indexing (`parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) for massive speedups (measured ~30x here) when indices logically map directly to colormap list indexes.
