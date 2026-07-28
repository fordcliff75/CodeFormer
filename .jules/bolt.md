## 2024-07-28 - Bottleneck in Element-wise Mapping
**Learning:** Iterative Python loops executing element-wise checking against large numpy arrays (e.g., `out == idx` for 512x512 maps) introduce significant CPU bottlenecks in model inference pipelines.
**Action:** Replace them with C-level NumPy advanced indexing (e.g., `np.array(colormap, dtype=float)[out]`) to drastically improve throughput.
