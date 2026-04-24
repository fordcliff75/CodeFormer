## 2026-04-24 - tensor2img_fast conditional squeeze and rounding
**Learning:** tensor2img has overhead from loops and grid logic. tensor2img_fast is faster for single images but truncates instead of rounding, and an unconditional `squeeze(0)` strips the channel dimension if c=1.
**Action:** Use tensor2img_fast across inference scripts for performance gains. Update tensor2img_fast to conditionally squeeze when `dim() == 4` and use `.round()` before casting to uint8.
