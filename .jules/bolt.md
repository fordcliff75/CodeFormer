## 2024-07-21 - [Optimize mask colormap mapping]
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., `out == idx`) introduce significant CPU bottlenecks.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., `np.array(COLORMAP)[out]`) to drastically improve throughput.
