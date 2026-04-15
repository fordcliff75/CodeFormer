## 2024-05-15 - Fast tensor to image conversion
**Learning:** Using `tensor2img_fast` for single-image post-processing avoids slower generic logic in `tensor2img`. However, standard `tensor2img_fast` defaults truncate when casting to `uint8`, causing fatal image quality regressions, and unconditional `.squeeze(0)` fails if a grayscale image doesn't have a batch dimension.
**Action:** Use `.round().type(torch.uint8)` in `tensor2img_fast`, conditionally check `tensor.dim() == 4` before `.squeeze(0)`, and substitute it in inference scripts to improve performance safely.
