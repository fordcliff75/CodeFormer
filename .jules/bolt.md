# Bolt's Journal

## 2024-05-23 - Optimization of Image Restoration Loop
**Learning:** `torch.cuda.empty_cache()` inside an inference loop forces CPU-GPU synchronization, severely impacting performance. Removing it allows for pipelining. Also, `tensor2img` can be optimized by performing operations on the GPU (or Tensor) and converting to `uint8` before moving to CPU (numpy), reducing data transfer size by 4x.
**Action:** Always check for `empty_cache()` in loops and remove it unless strictly necessary for OOM avoidance (which should be handled by batch size or gradient accumulation, not per-sample clearing). Use optimized tensor-to-image conversion when possible.
