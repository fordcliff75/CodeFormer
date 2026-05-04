## 2024-05-18 - [PyTorch GPU to CPU PCIe bottleneck]
**Learning:** Moving 32-bit float tensors from GPU to CPU to perform image math (clamping, normalizing, rounding, and type casting) is a significant performance bottleneck due to PCIe bus bandwidth limits.
**Action:** Move the `clamp`, `round`, and `type(torch.uint8)` operations to the GPU BEFORE calling `.cpu()`. This reduces the amount of data transferred across the PCIe bus by exactly 4x (32-bit to 8-bit), measurably speeding up post-processing in inference scripts.
