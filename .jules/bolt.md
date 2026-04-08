## 2024-04-08 - GPU Post-processing and PCIe bottleneck
**Learning:** Performing tensor-to-image post-processing (scaling, rounding, casting to uint8) on the GPU before transferring to CPU reduces data sent across the PCIe bus by 4x (from 32-bit floats to 8-bit integers), avoiding a common PyTorch performance bottleneck.
**Action:** Use `tensor2img_fast` instead of `tensor2img` for single images, ensuring it uses `.round()` before casting to `uint8` to avoid fatal image regressions. Also remember to conditionally handle `.squeeze(0)` to prevent channel stripping for grayscale images.

## 2024-04-08 - Video processing peak memory
**Learning:** Buffering all frames of a video in memory (O(N) relative to frame count) instead of streaming them directly to a `VideoWriter` causes immense peak memory usage and out-of-memory errors on large videos.
**Action:** Read and write video frames iteratively to achieve O(1) peak memory usage.
