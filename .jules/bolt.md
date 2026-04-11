## 2026-04-11 - [Remove empty_cache in GPU inference loops]
**Learning:** Calling `torch.cuda.empty_cache()` within an inference loop severely degrades performance by forcing a global CPU-GPU synchronization and forcing the caching allocator to return memory to the OS, disabling PyTorch's efficient memory management.
**Action:** Proactively remove `empty_cache` calls from critical paths (like per-frame or per-image loops) and replace generic post-processing functions (like `tensor2img`) with optimized, GPU-to-CPU efficient versions (`tensor2img_fast`) that safely handle channel dimensions.
