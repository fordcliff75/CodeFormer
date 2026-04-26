## 2024-04-26 - tensor2img performance
**Learning:** `tensor2img` is much slower than `tensor2img_fast` because it creates a grid using `make_grid` even for single images, transfers back and forth to cpu, and allocates lists.
**Action:** Replace `tensor2img` with `tensor2img_fast` in inference scripts (CodeFormer, inpainting, colorization). To avoid truncation issues, add `.round()` before casting to `uint8` in `tensor2img_fast` to match `tensor2img`. Also gracefully handle 1-channel images.
