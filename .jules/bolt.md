## 2024-10-24 - [Avoid empty_cache in inference loops]
**Learning:** The codebase frequently uses `torch.cuda.empty_cache()` inside inference loops (e.g., after processing each face). This forces synchronization and adds significant overhead without real benefit for standard inference.
**Action:** Remove `torch.cuda.empty_cache()` from loops. Only use it when OOM is imminent or at the end of large batch processing.
