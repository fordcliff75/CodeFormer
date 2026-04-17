## 2024-05-24 - Avoid global GPU synchronization in loops
**Learning:** Calling `torch.cuda.empty_cache()` inside loops (like inference loops) forces global GPU synchronization and releases memory to the OS, preventing the PyTorch caching allocator from efficiently reusing memory. This causes massive slowdowns.
**Action:** Remove `torch.cuda.empty_cache()` from critical paths and tight loops during optimization to allow PyTorch's memory allocator to work properly.
