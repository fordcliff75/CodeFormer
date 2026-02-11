import sys
import os
import time
import torch
import numpy as np
import cv2

# Add the root directory to sys.path so we can import basicsr
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from basicsr.utils.img_util import tensor2img, tensor2img_fast

def verify_tensor2img():
    # Setup
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Running on {device}")

    # Create a random tensor mimicking inference output (1, 3, 512, 512)
    # Values in range [-1, 1]
    tensor = torch.randn(1, 3, 512, 512).to(device).clamp_(-1, 1)

    # Warmup
    print("Warming up...")
    for _ in range(10):
        _ = tensor2img(tensor, min_max=(-1, 1))
        _ = tensor2img_fast(tensor, min_max=(-1, 1))

    # Test tensor2img
    print("Benchmarking tensor2img...")
    start_time = time.time()
    for _ in range(100):
        out1 = tensor2img(tensor, min_max=(-1, 1))
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    time1 = time.time() - start_time

    # Test tensor2img_fast
    print("Benchmarking tensor2img_fast...")
    start_time = time.time()
    for _ in range(100):
        out2 = tensor2img_fast(tensor, min_max=(-1, 1))
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    time2 = time.time() - start_time

    print(f"tensor2img time (100 runs): {time1:.4f}s")
    print(f"tensor2img_fast time (100 runs): {time2:.4f}s")
    if time2 > 0:
        print(f"Speedup: {time1/time2:.2f}x")
    else:
        print("Speedup: Infinite (too fast to measure)")

    # Compare outputs
    # Note: currently tensor2img_fast floors, while tensor2img rounds.
    # So we expect some differences.
    diff = np.abs(out1.astype(np.float32) - out2.astype(np.float32))
    max_diff = np.max(diff)
    mean_diff = np.mean(diff)
    print(f"Max difference: {max_diff}")
    print(f"Mean difference: {mean_diff}")

    if max_diff > 1.01: # allow float errors slightly above 1
        print("FAIL: Significant difference detected!")
    elif max_diff > 0:
        print("WARN: Minor difference detected (likely due to rounding vs flooring).")
    else:
        print("PASS: Outputs are identical.")

if __name__ == "__main__":
    verify_tensor2img()
