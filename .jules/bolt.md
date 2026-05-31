## 2024-06-25 - Replace `tensor2img` with `tensor2img_fast`
**Learning:** The `tensor2img` function has overhead from looping and `make_grid` logic. The repository includes an explicitly optimized version, `tensor2img_fast`, which is faster for single-image conversions but was not fully utilized in inference scripts.
**Action:** Replace `tensor2img` with `tensor2img_fast` in inference scripts (`inference_codeformer.py`, `inference_colorization.py`, `inference_inpainting.py`) and remember to import it and update the `except` blocks as well to maintain robustness.
