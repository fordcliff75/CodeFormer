## 2026-08-24 - Optimize Parsing Mask Creation Using NumPy Advanced Indexing
**Learning:** During model inference, an iterative Python loop executing element-wise checking (`out == idx`) against a large numpy array (512x512) introduces significant CPU bottleneck overhead (taking ~0.014s).
**Action:** Replace slow iterative Python loops and boolean indexing with C-level NumPy advanced indexing (e.g., `np.array(MASK_COLORMAP, dtype=float)[out]`) to dramatically improve throughput (drops to ~0.002s). Avoid redundant `np.zeros()` initializations when the entire array is going to be populated.
