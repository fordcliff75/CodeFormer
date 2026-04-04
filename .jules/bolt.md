
## 2024-05-24 - Tensor Post-Processing Performance Bottleneck
**Learning:** Performing tensor-to-image post-processing (clamping, scaling, rounding, casting to uint8) on the CPU via `tensor2img` is significantly slower and sends 4x more data across the PCIe bus (32-bit floats vs 8-bit integers) compared to processing it on the GPU before transfer. However, `tensor2img_fast` was missing a `.round()` call, causing image quality regressions by truncating instead of rounding.
**Action:** Use `tensor2img_fast` instead of `tensor2img` for post-processing single-image tensors across inference scripts, ensuring it includes `.round()` before casting to `uint8` to match `tensor2img` quality without losing the performance benefit.
