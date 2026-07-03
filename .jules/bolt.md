## 2025-01-20 - NumPy Advanced Indexing for Colormaps
**Learning:** During model inference, iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps for face colormapping) introduce significant CPU bottlenecks compared to C-level NumPy operations.
**Action:** Replace iterative boolean mask assignments (`mask[out == idx] = color`) with NumPy advanced indexing (`np.array(COLORMAP)[out]`) to reduce time complexity and significantly improve throughput.
