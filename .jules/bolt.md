## 2024-11-20 - [Performance bottleneck in NumPy array mapping]
**Learning:** In python, mapping array values using a `for` loop that iterates over a colormap and applies boolean indexing one class at a time is an O(N_classes * Pixels) operation, taking roughly 15ms per image for 19 classes.
**Action:** Replace slow boolean loops mapping class IDs to colors with vectorized O(Pixels) NumPy advanced indexing (e.g. `np.array(MASK_COLORMAP)[out]`) for an instant 10x speedup in CPU inference bounds.
