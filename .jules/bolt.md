## 2024-05-14 - Optimize face parsing mask creation
**Learning:** Iterative Python loops executing element-wise checks (`out == idx`) against large NumPy arrays (e.g., 512x512) for every semantic class introduce significant CPU bottlenecks during model inference.
**Action:** Replace Python-level iteration and array boolean masking with C-level NumPy advanced indexing (`array[indices]`) to dramatically reduce algorithmic complexity and inference time.
