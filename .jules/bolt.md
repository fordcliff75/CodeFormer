## 2024-04-10 - [Optimize tensor2img memory usage]
**Learning:** PyTorch models running inference often inadvertently trigger full GPU synchronization when global functions like `torch.cuda.empty_cache()` are used inside execution loops, and `tensor2img` can be slow due to rounding issues and float conversions before offloading to CPU.
**Action:** Replace `tensor2img` with `tensor2img_fast` globally across inference scripts, remove `torch.cuda.empty_cache()` inside hot paths to avoid CUDA sync overhead, and ensure `tensor2img_fast` conditionally squeezes to handle c=1 efficiently.
