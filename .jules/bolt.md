## 2024-06-18 - [Face Mask Colormap Array Indexing]
**Learning:** Using iterative Python loops to construct segmentation masks over large NumPy arrays (e.g., iterating classes and doing `mask[out == idx] = color`) is an extreme performance bottleneck due to $O(C \times N)$ time complexity and loop overhead.
**Action:** Always replace Python iteration with C-optimized NumPy advanced indexing (`np.array(Colormap)[out]`) for mapping indices to values. It reduces complexity to $O(N)$ and yields ~5x faster execution, drastically improving inference pipeline throughput.
