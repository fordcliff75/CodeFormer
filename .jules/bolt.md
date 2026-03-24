## 2024-03-24 - [Avoid Global GPU Sync inside Inference Loops]
**Learning:** Calling `torch.cuda.empty_cache()` inside an inference loop causes massive performance degradation by forcing global CPU/GPU synchronization and destroying PyTorch's caching memory allocator mechanism, which is critical for iteration speed.
**Action:** Always verify that inference loops rely on `del` for tensors and do not call `empty_cache()` explicitly inside the loop unless strictly catching an OutOfMemory error.
