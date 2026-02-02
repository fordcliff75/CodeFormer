## 2025-02-17 - Project Setup Nuances
**Learning:** The project relies on `basicsr` which is a local package but requires `basicsr/version.py` to be generated. The provided `setup.py` assumes a certain environment or pip behavior that might fail in some contexts (like missing git or running from root with modern pip/setuptools). Also, `basicsr` is not installed in the environment but expected to be in PYTHONPATH.
**Action:** When working with this repo, ensure `basicsr/version.py` exists (can be dummy) and add `.` to `PYTHONPATH` before running scripts.

## 2025-02-17 - Performance Bottleneck Identified
**Learning:** The inference scripts `inference_codeformer.py`, `inference_inpainting.py`, and `inference_colorization.py` all call `torch.cuda.empty_cache()` inside the inference loop. This is a known anti-pattern that causes unnecessary GPU synchronization and overhead, significantly slowing down processing, especially for batches of images.
**Action:** Remove `torch.cuda.empty_cache()` from inference loops.

## 2025-02-17 - Optimized Tensor Conversion
**Learning:** `basicsr.utils.img_util` provides a `tensor2img_fast` function which is faster than `tensor2img` for single image tensors (1, C, H, W). The inference scripts process images sequentially so this optimized function can be used instead of the generic one.
**Action:** Replace `tensor2img` with `tensor2img_fast` in inference loops.
