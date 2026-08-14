## 2025-02-23 - Fast Face Parsing Colormap Mapping
**Learning:** Using an iterative python loop to element-wise check and set array elements based on large image masks (e.g. 512x512) introduces a significant CPU bottleneck.
**Action:** Replace `out == idx` loops with C-level NumPy advanced indexing (e.g. `np.array(COLORMAP)[out]`) for massive speedups in image manipulation.
