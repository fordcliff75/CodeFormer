## 2024-10-24 - [Replace O(N) segmentation loop with NumPy Advanced Indexing]
**Learning:** In model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g. 512x512 segmentation maps via `out == idx`) introduce significant CPU bottlenecks.
**Action:** Replace them with C-level NumPy advanced indexing (e.g. `parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]`) to dramatically improve throughput.
