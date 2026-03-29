## 2024-05-18 - Removed torch.cuda.empty_cache() and used tensor2img_fast
**Learning:** Found that `tensor2img_fast` was already defined in `basicsr/utils/img_util.py` but not exported in `__init__.py`, making it inaccessible. We removed `torch.cuda.empty_cache()` from inference loops to prevent global GPU synchronization and used `tensor2img_fast` instead of `tensor2img` to post-process single-image tensors 4x faster on GPU before moving to CPU.
**Action:** Always check if a faster function exists but is simply not exported. Remove `torch.cuda.empty_cache()` inside loops.
