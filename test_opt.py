import numpy as np
import time

out = np.random.randint(0, 19, size=(512, 512))

start = time.perf_counter()
parse_mask1 = np.zeros(out.shape)
MASK_COLORMAP = [0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 255, 0, 0, 0]
for idx, color in enumerate(MASK_COLORMAP):
    parse_mask1[out == idx] = color
time1 = time.perf_counter() - start

start = time.perf_counter()
# ⚡ Bolt Optimization: Replace O(N_classes * Image_Size) iterative loop
# over mask indexing with O(Image_Size) NumPy advanced indexing to avoid CPU bottlenecks.
parse_mask2 = np.array(MASK_COLORMAP, dtype=float)[out]
time2 = time.perf_counter() - start

print(f"Original: {time1:.6f}s")
print(f"Optimized: {time2:.6f}s")
print(f"Match: {np.array_equal(parse_mask1, parse_mask2)}")
