## 2024-05-18 - NumPy Advanced Indexing Optimization
**Learning:** Iterating over segmentation classes in Python using boolean masking (`out == idx`) on large NumPy arrays is a severe CPU bottleneck. NumPy advanced indexing (`np.array(colormap)[out]`) is exponentially faster.
**Action:** Always prefer C-level NumPy advanced indexing over Python loops when mapping integer indices (like segmentation maps) to colors or arrays.
