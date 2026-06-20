
## 2025-02-12 - Optimize Face Parsing Mask Generation
**Learning:** In PyTorch/NumPy computer vision pipelines (like Face Restoration Helper), iterative Python loops executing element-wise checking against large numpy arrays (e.g., 512x512 segmentation maps via `parse_mask[out == idx] = color`) introduce massive CPU bottlenecks, turning constant-time mapping into O(N_classes * Image_Size).
**Action:** Always replace explicit enumeration over colormaps with C-level NumPy advanced indexing (e.g., `np.array(MASK_COLORMAP, dtype=float)[out]`), which operates natively in O(Image_Size) and reduces mask generation time by over 30x.
