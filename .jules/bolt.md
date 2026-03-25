## 2024-05-24 - [Optimize tensor2img post-processing]
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU before transferring to CPU reduces data sent across the PCIe bus by 4x.
**Action:** Use `tensor2img_fast` with `.round()` instead of the slower `tensor2img` for post-processing single-image tensors across inference scripts.
