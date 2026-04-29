## 2024-05-18 - [Use tensor2img_fast instead of tensor2img]
**Learning:** The `tensor2img` function has overhead from looping and `make_grid` logic. Substituting it with `tensor2img_fast` for single-image conversions significantly improves performance by bypassing these steps. `tensor2img_fast` must conditionally handle squeezing 3D vs 4D tensors.
**Action:** Use `tensor2img_fast` and explicitly check tensor dimensionality before calling `.squeeze(0)`.
