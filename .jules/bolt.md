## 2025-02-25 - Advanced NumPy Indexing over Iterative Masking
**Learning:** Iterating over mask categories to apply colormaps in python (e.g., `parse_mask[out == idx] = color`) on large numpy arrays creates significant CPU bottlenecks during ML inference post-processing.
**Action:** Replace iterative boolean masking with C-level NumPy advanced indexing (`np.array(MASK_COLORMAP, dtype=float)[out]`) to process all classes simultaneously and achieve massive speedups (~30x for 19 classes).
