## YYYY-MM-DD - [Vectorizing Mask Colormap Mapping]
**Learning:** Iterating over `MASK_COLORMAP` and indexing a 512x512 array 19 times is inefficient in Python and introduces a CPU bottleneck.
**Action:** Replace the iterative loop with NumPy advanced indexing `parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]` to dramatically improve throughput.
