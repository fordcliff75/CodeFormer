## 2024-04-02 - GPU Bottlenecks in Post-Processing
**Learning:** Performing tensor-to-image conversions on the CPU via `tensor2img` is slow because it causes PCIe bottlenecks and `torch.cuda.empty_cache()` inside loops causes global GPU synchronization that prevents allocator memory reuse.
**Action:** Always perform scaling, rounding, and clamping on the GPU before sending data back to the CPU, and remove `torch.cuda.empty_cache()` from critical inference loops.
