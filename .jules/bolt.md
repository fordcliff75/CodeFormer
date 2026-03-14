## 2026-03-14 - [Use tensor2img_fast instead of tensor2img]
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU/tensor-side before transferring to CPU is significantly faster than transferring float tensors to CPU and processing there.
**Action:** Use `tensor2img_fast` instead of `tensor2img` when post-processing single-image tensors to maintain optimal performance.
