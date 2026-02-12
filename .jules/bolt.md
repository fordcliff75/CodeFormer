## 2024-02-26 - GPU Tensor Processing
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU before transferring to CPU is significantly faster (approx 1.6x) than transferring float tensors, as it reduces PCIe bandwidth usage by 4x.
**Action:** When implementing or optimizing `tensor2img` functions, ensure mathematical operations and type casting happen on the source device (GPU) before `.cpu()` transfer.
