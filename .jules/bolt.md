## 2024-09-08 - Optimize face mask parsing
**Learning:** Iterative Python loops on large numpy arrays (e.g., 512x512 segmentation maps) introduce significant CPU bottlenecks. Replacing them with C-level NumPy advanced indexing improves throughput significantly.
**Action:** Always prefer vectorized operations or NumPy advanced indexing over element-wise loops for heavy image processing tasks in Python.
