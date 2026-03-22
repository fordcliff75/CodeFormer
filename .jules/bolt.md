
## 2024-05-28 - GPU Post-Processing Performance
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU before transferring to CPU reduces data sent across the PCIe bus by 4x, avoiding a common PyTorch performance bottleneck. `tensor2img_fast` achieves this but needs `.round()` to maintain quality parity with `tensor2img`.
**Action:** Use `tensor2img_fast` instead of the slower `tensor2img` for post-processing single-image tensors across inference scripts, ensuring `.round()` is applied before type casting.
