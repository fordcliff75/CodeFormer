
## 2024-05-23 - NumPy Advanced Indexing vs Loops
**Learning:** In `facelib/utils/face_restoration_helper.py`, a `for` loop over 19 colormap classes to conditionally update a 512x512 mask array is slow (takes ~1.1s for 100 loops vs ~0.03s for indexing).
**Action:** Use NumPy advanced indexing `parse_mask = np.array(MASK_COLORMAP, dtype=float)[out]` to eliminate Python-level iteration and conditionally updating arrays.
