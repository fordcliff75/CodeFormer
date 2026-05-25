## 2024-06-25 - Vectorize colormap mapping in FaceRestorationHelper
**Learning:** In PyTorch/NumPy computer vision pipelines, manually mapping class indices to colors using iterative boolean masks (`parse_mask[out == idx] = color`) is $O(N \times C)$ and highly inefficient. NumPy advanced array indexing (`np.array(COLORMAP)[out]`) reduces this to an $O(N)$ operation natively in C.
**Action:** When working with segmentation or parse masks, always look for opportunities to replace explicit loops over class indices with vectorized array indexing or PyTorch operations.
