## 2024-05-19 - Fast Image Tensor Conversion
**Learning:** `tensor2img_fast` offers a significant performance improvement over `tensor2img` for single image tensors (shape `1, c, h, w`). It does this by directly moving scaled tensors to `.type(torch.uint8)` before `.cpu().numpy()`, keeping operations on the GPU as long as possible.
**Action:** Replace `tensor2img` with `tensor2img_fast` in critical paths like inference loops.
