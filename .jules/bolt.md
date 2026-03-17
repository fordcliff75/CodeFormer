## 2024-05-18 - GPU Post-processing and Synchronization
**Learning:** Using `torch.cuda.empty_cache()` inside PyTorch inference loops forces a global GPU synchronization and releases memory back to the OS, defeating the caching allocator. Additionally, post-processing float tensors to uint8 on the GPU before sending them to the CPU via PCIe saves 4x bandwidth compared to sending float tensors first and processing on CPU.
**Action:** Always verify if `tensor2img_fast` can replace `tensor2img` and ensure `torch.cuda.empty_cache()` is removed from inner loops.
