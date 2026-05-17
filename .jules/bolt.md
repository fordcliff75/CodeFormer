## 2024-05-30 - tensor2img_fast channel dimension drop and rounding truncation
**Learning:**  can unintentionally drop the channel dimension for 1-channel images when calling  directly without checking . Additionally, converting floats to uint8 directly without calling  truncates the values, causing pixel-level visual differences compared to the slower .
**Action:** Always verify  when squeezing batch dimensions, and explicitly  before casting float tensors to integer types to maintain visual fidelity during image conversions.
## 2024-05-30 - tensor2img_fast channel dimension drop and rounding truncation
**Learning:** `tensor2img_fast` can unintentionally drop the channel dimension for 1-channel images when calling `.squeeze(0)` directly without checking `.dim() == 4`. Additionally, converting floats to uint8 directly without calling `.round()` truncates the values, causing pixel-level visual differences compared to the slower `tensor2img`.
**Action:** Always verify `.dim()` when squeezing batch dimensions, and explicitly `.round()` before casting float tensors to integer types to maintain visual fidelity during image conversions.
