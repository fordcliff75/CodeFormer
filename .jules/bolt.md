## 2024-04-19 - Replace tensor2img with tensor2img_fast
**Learning:** `tensor2img_fast` is a faster alternative to `tensor2img` for single-image conversion in inference scripts. It bypasses nested loops and grid making logic.
**Action:** Replace `tensor2img` with `tensor2img_fast` in inference scripts (`inference_codeformer.py`, `inference_colorization.py`, `inference_inpainting.py`) to speed up inference post-processing.
