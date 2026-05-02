
## 2024-05-18 - [Python Built-ins Overhead in Tight Loops]
**Learning:** In very tight inner loops evaluating geometry or mathematical bounds (like face bounding boxes), calling Python built-ins like `max()` or `min()` or nested helper functions causes significant function call overhead that compounds over large arrays. Using simple, direct inline `if-else` variable assignments or sequential conditional assignments (e.g. `val = x if x >= 0 else 0; val = w if val > w else val`) avoids this overhead and provides measurable speedups.
**Action:** When refactoring nested mathematical loops in performance-critical code (e.g. `facelib`), prioritize inline sequential conditions or vectorized operations over deep Python function/built-in invocation.

## 2024-05-18 - [NumPy Overhead for Simple Math]
**Learning:** Using `np.array` instantiations and `np.linalg.norm` for simple distance comparisons (like Euclidean distance to find a minimum) introduces significant overhead in a loop. Calculating purely squared Euclidean distance mathematically (e.g., `(dx)**2 + (dy)**2`) with native Python float operations directly inside the loop yields the exact same logical result for minimum distance comparisons but is vastly faster (~12x observed in benchmarks).
**Action:** Avoid instantiating `NumPy` objects inside hot loops just for simple geometric calculations or comparisons when native Python math can achieve the same result faster.
