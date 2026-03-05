
## 2024-03-05 - Avoid torch.cuda.empty_cache() in tight loops
**Learning:** Calling `torch.cuda.empty_cache()` inside the inference loop forces global GPU synchronization and releases memory to the OS, which defeats PyTorch's caching allocator. This leads to severe performance degradation during bulk image processing.
**Action:** Remove `torch.cuda.empty_cache()` from inner processing loops to allow PyTorch to efficiently manage memory allocations.

## 2024-03-05 - Optimize tensor-to-image processing on GPU
**Learning:** The default `tensor2img` converts float tensors to numpy arrays on CPU before scaling and rounding. By contrast, `tensor2img_fast` processes data directly on the GPU (scaling, rounding, clamping) and then transfers `uint8` tensors to CPU, reducing transfer size significantly and leveraging parallel computation.
**Action:** Use `tensor2img_fast` (or perform tensor scaling and casting to uint8 before `.cpu().numpy()`) to minimize PCI-e bottleneck overhead when saving images.
