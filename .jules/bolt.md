
## 2024-05-17 - PyTorch Global Synchronization Anti-Pattern
**Learning:** Calling `torch.cuda.empty_cache()` inside an inference loop forces implicit CPU-GPU synchronization and thrashes the caching allocator, severely degrading performance. PyTorch automatically manages memory inside loops.
**Action:** Always verify that `torch.cuda.empty_cache()` is not used within tight execution loops like inference scripts. Remove it to allow the PyTorch caching allocator to work efficiently.

## 2024-05-17 - Tensor to Image Conversion Bottleneck
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU before transferring to CPU reduces data sent across the PCIe bus by 4x (from 32-bit floats to 8-bit integers).
**Action:** Use PyTorch's native `.round().type(torch.uint8).cpu()` rather than performing these casts via NumPy on the CPU side to optimize PCIe bandwidth.
