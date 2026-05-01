import torch
import numpy as np
import cv2
import time
from basicsr.utils.img_util import tensor2img, tensor2img_fast

t = torch.rand(1, 3, 512, 512).cuda() if torch.cuda.is_available() else torch.rand(1, 3, 512, 512)

# Warmup
tensor2img(t)
tensor2img_fast(t)

start = time.time()
for _ in range(100):
    tensor2img(t)
t1 = time.time() - start

start = time.time()
for _ in range(100):
    tensor2img_fast(t)
t2 = time.time() - start

print(f"tensor2img: {t1:.4f}s")
print(f"tensor2img_fast: {t2:.4f}s")
print(f"Speedup: {t1/t2:.2f}x")
