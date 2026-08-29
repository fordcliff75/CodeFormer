## YYYY-MM-DD - O(1) Numpy advanced indexing over O(N) for loops
**Learning:** Python iterative loops over large Numpy arrays (like a 512x512 face parse mask) create significant CPU bottlenecks in ML inference pipelines, taking >1.0s vs 0.05s.
**Action:** Always use Numpy advanced indexing (`arr[indices]`) instead of boolean masks and iteration for element-wise mapping.
