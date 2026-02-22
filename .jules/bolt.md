## 2024-05-23 - [Remove Empty Cache in Loops]
**Learning:** `torch.cuda.empty_cache()` was used inside inference loops, forcing constant GPU synchronization and degrading performance.
**Action:** Always check for `empty_cache()` calls in tight loops and remove them unless strictly necessary for OOM handling.
