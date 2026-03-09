## 2024-03-09 - Remove torch.cuda.empty_cache() inside loops
**Learning:** Calling `torch.cuda.empty_cache()` inside an inference loop forces global GPU synchronization and releases memory to the OS, preventing the PyTorch caching allocator from efficiently reusing memory, which causes significant performance degradation.
**Action:** Remove `torch.cuda.empty_cache()` from critical paths like inference loops. Let PyTorch manage GPU memory.

## 2024-03-09 - Direct-to-Device Allocation
**Learning:** Allocating tensors like `torch.zeros(..., device=device)` directly on the target device prevents costly CPU-to-GPU data transfers and improves performance.
**Action:** Always specify the `device` argument when creating new tensors inside performance-critical code.

## 2024-03-09 - tensor2img_fast vs tensor2img
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU/tensor-side using `tensor2img_fast` is significantly faster than using the CPU-bound `tensor2img`. However, `tensor2img_fast` required adding `.round()` before casting to `uint8` to match the exact output quality of `tensor2img`.
**Action:** Use `tensor2img_fast` for post-processing single-image tensors to maintain optimal performance, ensuring `.round()` is applied before `uint8` casting to avoid color truncation artifacts.
