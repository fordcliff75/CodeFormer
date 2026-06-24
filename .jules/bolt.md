
## 2024-05-18 - tensor2img performance bottleneck
**Learning:** `tensor2img` has high overhead from internal `make_grid` loops that drastically slow down inference post-processing. Additionally, naive PyTorch `.squeeze(0)` calls on 3D output arrays without dim checks might accidentally strip required single-channel dimensions on grayscale images.
**Action:** When working on optimized image-to-tensor pipelines, use conditional fast paths that verify dimensions (`tensor.dim() == 4`) before executing tensor shaping logic and bypass slow generic grids.
