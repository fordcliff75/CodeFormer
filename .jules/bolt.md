## 2026-02-23 - [PyTorch empty_cache Overhead]
**Learning:** PyTorch's `cuda.empty_cache()` forces full device synchronization and releases all cached memory back to the OS, which is extremely slow when called inside inference loops. The PyTorch caching allocator is designed to reuse memory efficiently without manual intervention.
**Action:** Always scan for `torch.cuda.empty_cache()` inside hot loops and remove it unless absolutely necessary for OOM prevention on severely constrained hardware.
