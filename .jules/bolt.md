## 2024-05-24 - [Replace tensor2img with tensor2img_fast]
**Learning:** The tensor2img function has a performance bottleneck due to checking shapes and calling make_grid inside loops. The `tensor2img_fast` function provides a much faster approach.
**Action:** Replace `tensor2img` with `tensor2img_fast` in inference scripts. Update `tensor2img_fast` to round up properly and handle 1 channel properly so quality matches. And export it.
